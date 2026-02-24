import requests
import json
import pandas as pd

# Base URL for your layer
base_url = "https://services9.arcgis.com/xSsJeibXqRtsnmY7/ArcGIS/rest/services/Hydrogen_Infrastructure_Map_2024Q4_WFL1/FeatureServer/7/query"

# Function to fetch all features in batches
def fetch_all_features(batch_size=2000):
    all_features = []
    result_offset = 0

    while True:
        params = {
            "where": "1=1",
            "outFields": "*",
            "returnGeometry": "false",  # Set to True if you want geometry
            "f": "json",
            "resultRecordCount": batch_size,
            "resultOffset": result_offset
        }

        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        features = data.get("features", [])
        if not features:
            break

        all_features.extend(features)
        print(f"Fetched {len(features)} features (offset {result_offset})")
        result_offset += len(features)

    return all_features

# Fetch all features from the server
features = fetch_all_features()

# Extract attributes only
rows = [feature["attributes"] for feature in features]

# Create dataframe
df = pd.DataFrame(rows)

# Set OBJECTID as index
df.set_index("OBJECTID", inplace=True)

# Map TSO_dict to countries
TSO_dict = {
    'GASCADE Gastransport GmbH (Fluxys)': "DE/BE",
    'eustream, a.s.': "SK",
    'SNTGN Transgaz SA': "RO",
    'FGSZ Ltd.': "HU",
    'LLC Gas TSO of Ukraine (Eustream s.a. - NET4GAS s.r.o. - Open Grid Europe GmbH)': "UA/DE/CZ/SK",
    'NET4GAS, s.r.o.': "CZ",
    'Gasunie Deutschland Transport Services GmbH': "DE",
    'Natran': "FR",
    'ONTRAS Gastransport GmbH and VNG Gasspeicher GmbH': "DE",
    'Nowega GmbH': "DE",
    'TAG GmbH': "AT",
    'Bulgartransgaz EAD': "BG",
    'Fluxys Belgium and Pipelink': "BE",
    'Natran (French side)': "FR",
    'Elering AS': "EE",
    'ONTRAS Gastransport GmbH': "DE",
    'GASCADE Gastransport GmbH': "DE",
    'AB Amber Grid': "LT",
    'Conexus Baltic Grid, JSC': "LV",
    'GAZ-SYSTEM S.A.': "PL",
    'Fluxys Belgium': "BE",
    'REN': "PT",
    'Enagás Infraestructuras de Hidrógeno/Terega/Natran/Open Grid Europe': "ES/FR/DE",
    'Thyssengas GmbH': "DE",
    'PLINACRO Ltd.': "HR",
    'GASCADE Gastransport GmbH and terranets bw': "DE",
    'NOGAT B.V.': "NL",
    'Noordgastransport B.V. (NGT)': "NL",
    'H2Pole, S.L.U. (Reganosa)': "ES",
    'GASCADE Gastransport GmbH, Ontras GmbH': "DE",
    'Gastransport Nord GmbH': "DE",
    'FluxSwiss': "CH",
    'Plinacro Ltd': "HR",
    'PLINOVODI d.o.o.': "SI",
    'N.V. Nederlandse Gasunie': "NL",
    'A/S Norske Shell (coordinator), Aker Horizons AS, CapeOmega AS and Gassco AS': "NO",
    'Gasgrid Vetyverkot Oy , GASCADE Gastransport GmbH, Copenhagen Energy Islands AS': "FI/DE/DK",
    'REN - Gasodutos, S.A.': "PT",
    'Gas Connect Austria GmbH': "AT",
    'Snam Rete Gas S.p.A.': "IT",
    'DESFA SA': "GR",
    'Ferngas Netzgesellschaft mbH': "DE",
    'Ferngas Netzgesellschaft mbH/\nGASCADE Gastransport GmbH': "DE",
    'Creos Luxembourg S.A.': "LU",
    'bayernets GmbH': "DE",
    'Open Grid Europe GmbH': "DE",
    'Gasgrid Finland Oy': "FI",
    'Energinet': "DK",
    'Open Grid Europe GmbH, Fluxys TENP': "DE/BE",
    'Terega SA': "FR",
    'BadenovaNETZE GmbH, terranets bw': "DE",
    'Open Grid Europe GmbH; NaTran Deutschland GmbH': "DE",
    'Led by REN Gas, with the participation of REN Gasodutos, Floene, Bosch, Hylab, IST and INL': "PT",
    'H2GZ ENERGIZING': "PL",
    'Enagás Infraestructuras de Hidrogeno': "ES",
    'ICGB AD': "BG",
    'Gas Networks Ireland': "IE",
    'Snam  S.p.a.': "IT",
    'no data available': "UNKNOWN",
    'Gasunie Deutschland Transport Services GmbH, Thyssengas GmbH': "DE",
    'SeaCorridor': "UNKNOWN",
    'Green Energy Park Global B.V.\r\n': "NL",
    'Fluxys, National Gas': "BE/NL",
    'SGI': "UNKNOWN",
    'GASCADE': "DE",
    'BH Gas': "BA",
    'Plinacro': "HR",
    'IGI Poseidon': "IT/GR",
    'National Gas Transmission': "IE",
    'Gasgrid Vetyverkot Oy': "FI",
    'Without project developer': "UNKNOWN",
    'Cadent Gas Limited': "GB",
    'No data available': "UNKNOWN",
    'Creos Deutschland Wasserstoff GmbH': "DE",
    'Enagas Infraestructuras de Hidrogeno': "ES",
    'Nordion Energi AB': "SE",
    'Nowega GmbH, Open Grid Europe GmbH': "DE"
}

df['country'] = df['Promoter_N'].map(TSO_dict)

# Save to CSV
df.to_csv('pipeline_project.csv')
print(f"Saved {len(df)} records to pipeline_project.csv")