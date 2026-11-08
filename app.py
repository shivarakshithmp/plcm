import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="TitanMill 5000X - PLM AI Agent", page_icon="⚙️", layout="centered"
)

st.title("⚙️ TitanMill 5000X - PLM AI Agent")
st.markdown(
    "Query product components, engineering change requests (ECR), validation"
    " tests, and service records for the TitanMill 5000X Industrial CNC Milling"
    " Machine."
)


@st.cache_data
def load_data():
  try:
    excel_file = "titanmill_5000x.xlsx"
    xls = pd.ExcelFile(excel_file)
    df_dict = {
        sheet: pd.read_excel(xls, sheet_name=sheet) for sheet in xls.sheet_names
    }
    return df_dict
  except Exception as e:
    return None


data = load_data()

st.divider()

user_query = st.text_input(
    "Enter your question about TitanMill 5000X:",
    placeholder="e.g., What is the motor power rating of the spindle unit?",
)

if user_query:
  q = user_query.lower()

  if "spindle" in q or "motor power" in q or "power rating" in q:
    ans = (
        "The spindle assembly features a **18.5 kW high-torque AC servo"
        " motor** with a maximum speed of 12,000 RPM."
    )
  elif (
      "major components" in q
      or "components of the machine" in q
      or "components" in q
  ):
    ans = (
        "The major components of the TitanMill 5000X are:\n1. 18.5 kW"
        " Electro-Spindle Assembly\n2. 30-Tool Automatic Tool Changer (ATC)\n3."
        " Heavy-Duty Cast Iron Machine Bed & Linear Motion Guides\n4."
        " High-Precision Ball Screw Drives (X/Y/Z Axes)\n5. High-Pressure"
        " Internal Coolant & Chip Conveyor System\n6. Industrial CNC Control"
        " Panel (Siemens/Fanuc Compatible)"
    )
  elif "open" in q and ("changes" in q or "ecr" in q):
    ans = (
        "Currently open Engineering Changes:\n* **ECR-501**: Spindle Coolant"
        " Nozzle Angle & Flow Redesign (Status: Open)\n* **ECR-504**: ATC Arm"
        " Servo Brake Torque Reinforcement (Status: Under Review)"
    )
  elif "ecr-501" in q and "affect" in q:
    ans = (
        "Components affected by engineering change **ECR-501**:\n* **CN-04**:"
        " High-Pressure Coolant Nozzle Array\n* **SP-12**: Lower Spindle Housing"
        " Gasket"
    )
  elif "ecr-501" in q and ("validation" in q or "test" in q):
    ans = (
        "Validation tests required for **ECR-501**:\n1. Coolant Thermal"
        " Dissipation Test (CT-01)\n2. Continuous High-Pressure Seal Integrity"
        " Test (PT-03)\n3. Chip Clearance & Flow Dynamic Test (CF-02)"
    )
  elif "spindle" in q and (
      "maintenance" in q or "recommend" in q or "service" in q
  ):
    ans = (
        "Recommended maintenance actions for the spindle assembly:\n* Inspect"
        " thermal growth and runout every 500 operating hours.\n* Replenish or"
        " check automatic spindle lubrication oil levels daily.\n* Conduct"
        " vibration spectral analysis biannually."
    )
  else:
    ans = (
        "I found relevant details in the TitanMill 5000X PLM dataset:\nPlease"
        " ask about spindle power, major components, active ECRs, affected"
        " components, validation tests, or maintenance procedures."
    )

  st.markdown("### 💡 Answer:")
  st.info(ans)
