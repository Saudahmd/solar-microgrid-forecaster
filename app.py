import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/evaluate_matrix', methods=['POST'])
def evaluate_matrix():
    payload = request.get_json() or {}
    
    # Sensor telemetry inputs
    irrad = float(payload.get('irrad', 0.78))
    amb_temp = float(payload.get('amb_temp', 32.0))
    mod_temp = float(payload.get('mod_temp', 51.5))
    base_load = float(payload.get('base_load', 6500.0))
    bess_cap = float(payload.get('bess_cap', 10000.0))

    # PV Physics Derating Formula
    # Standard STC cell efficiency drops ~0.4% per °C over 25°C
    thermal_derate_factor = max(0.0, 1.0 - ((mod_temp - 25.0) * 0.004))
    
    # Peak Plant Capacity (22 Inverters Aggregated ~25,000 kW)
    theoretical_peak_kw = irrad * 24500.0
    current_gen_kw = theoretical_peak_kw * thermal_derate_factor
    thermal_loss_kw = theoretical_peak_kw - current_gen_kw

    # Asymmetric Prediction Horizons (p10 Floor, p90 Ceiling)
    p10_kw = max(0.0, current_gen_kw * 0.92)
    p90_kw = current_gen_kw * 1.07

    # Deficit / Microgrid Balancing Logic
    deficit_kw = round(max(0.0, base_load - p10_kw), 1)
    
    # Financial Impact: Commercial grid diesel peaker rate ~$0.34/kWh
    diesel_cost_saved = (min(current_gen_kw, base_load)) * 0.34

    # BESS Stress Category
    if deficit_kw == 0:
        stress = "Minimal (Idle / Charging)"
    elif deficit_kw < (bess_cap * 0.3):
        stress = "Low (Peak Shaving)"
    elif deficit_kw < (bess_cap * 0.6):
        stress = "Moderate (Discharge Ramp)"
    else:
        stress = "Severe (Peaker Required)"

    # Generate 24-Hour Diurnal Curve for the interactive Chart
    curve_hours = [f"{h:02d}:00" for h in range(24)]
    curve_median = []
    curve_p10 = []
    curve_p90 = []

    for h in range(24):
        if 6 <= h <= 18:
            # Diurnal solar bell curve
            solar_phase = np.sin(np.pi * (h - 6) / 12)
            h_gen = current_gen_kw * (solar_phase ** 1.35)
            curve_median.append(round(float(h_gen), 1))
            curve_p10.append(round(float(h_gen * 0.91), 1))
            curve_p90.append(round(float(h_gen * 1.08), 1))
        else:
            curve_median.append(0.0)
            curve_p10.append(0.0)
            curve_p90.append(0.0)

    return jsonify({
        'current_gen_kw': round(float(current_gen_kw), 1),
        'current_p10_kw': round(float(p10_kw), 1),
        'current_p90_kw': round(float(p90_kw), 1),
        'current_deficit_kw': deficit_kw,
        'thermal_derate_loss_kw': round(float(thermal_loss_kw), 1),
        'hourly_diesel_cost_saved': round(float(diesel_cost_saved), 2),
        'bess_stress_level': stress,
        'curve_hours': curve_hours,
        'curve_median': curve_median,
        'curve_p10': curve_p10,
        'curve_p90': curve_p90
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)