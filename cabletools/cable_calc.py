# Loss factor per 100 feet of cable based on cable type
# Losses are at 55MHz, 750MHz, 865MHz, and 1GHz
loss = {
    "RG6": [1.18, 5.65, 6.10, 6.55],
    "RG11": [0.96, 3.65, 3.98, 4.35],
    "FLEX500": [0.21, 2.23, 2.41, 2.59],
    "P3_500": [0.54, 2.16, 2.34, 2.52],
    "P3_625": [0.45, 1.78, 1.93, 2.08],
    "P3_875": [0.32, 1.29, 1.41, 1.53],
    "500MC": [0.49, 1.88, 2.05, 2.22],
    "750MC": [0.36, 1.29, 1.39, 1.51],
    "540QR": [0.48, 1.85, 2.00, 2.17],
    "860QR": [0.32, 1.24, 1.33, 1.44],
}

# For future use
passive_loss = {}


# Calculates loss based on footage, returns results at 4 frequencies in a list
def get_loss(footage, cable_type):
    results = []
    for values in loss[cable_type]:
        results.append(footage / 100 * values)
    return results
