import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Dry Bean Classification",
    page_icon="🌱",
    layout="wide"
)

# ============================================================
# MODEL PATH
# ============================================================

BASE_DIR = Path(r"C:\Users\spand\Desktop\mini projects\dry bean project")

MODEL_PATH = (
    BASE_DIR
    / "data set"
    / "DryBeanDataset"
    / "best_dry_bean_model.pkl"
)

# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

try:
    model = load_model()
except Exception as e:
    st.error("Unable to load the trained model.")
    st.write("Model path:")
    st.code(str(MODEL_PATH))
    st.exception(e)
    st.stop()

# ============================================================
# TITLE
# ============================================================

st.title("🌱 Dry Bean Classification System")

st.write(
    "This application predicts the dry bean variety "
    "using 16 morphological and geometric features."
)

st.divider()

# ============================================================
# IMPORTANT:
# THESE FEATURE NAMES MUST MATCH THE TRAINED MODEL EXACTLY
# ============================================================

features = [
    "Area",
    "Perimeter",
    "MajorAxisLength",
    "MinorAxisLength",
    "AspectRation",
    "Eccentricity",
    "ConvexArea",
    "EquivDiameter",
    "Extent",
    "Solidity",
    "roundness",
    "Compactness",
    "ShapeFactor1",
    "ShapeFactor2",
    "ShapeFactor3",
    "ShapeFactor4"
]

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("About the Project")

st.sidebar.write(
    """
    This project performs multi-class classification
    of dry beans.

    Possible classes:

    - Seker
    - Barbunya
    - Bombay
    - Cali
    - Dermason
    - Horoz
    - Sira
    """
)

st.sidebar.write(
    "Enter all 16 feature values and click Predict."
)

# ============================================================
# INPUT SECTION
# ============================================================

st.header("Enter Bean Measurements")

col1, col2, col3, col4 = st.columns(4)

# ============================================================
# COLUMN 1
# ============================================================

with col1:

    area = st.number_input(
        "Area",
        min_value=0.0,
        value=28395.0,
        step=100.0
    )

    perimeter = st.number_input(
        "Perimeter",
        min_value=0.0,
        value=610.291,
        step=1.0
    )

    major_axis = st.number_input(
        "MajorAxisLength",
        min_value=0.0,
        value=208.179,
        step=1.0
    )

    minor_axis = st.number_input(
        "MinorAxisLength",
        min_value=0.0,
        value=173.888,
        step=1.0
    )

# ============================================================
# COLUMN 2
# ============================================================

with col2:

    aspect_ratio = st.number_input(
        "AspectRation",
        min_value=0.0,
        value=1.197,
        step=0.001
    )

    eccentricity = st.number_input(
        "Eccentricity",
        min_value=0.0,
        max_value=1.0,
        value=0.549,
        step=0.001
    )

    convex_area = st.number_input(
        "ConvexArea",
        min_value=0.0,
        value=28715.0,
        step=100.0
    )

    equiv_diameter = st.number_input(
        "EquivDiameter",
        min_value=0.0,
        value=190.141,
        step=1.0
    )

# ============================================================
# COLUMN 3
# ============================================================

with col3:

    extent = st.number_input(
        "Extent",
        min_value=0.0,
        max_value=1.0,
        value=0.763,
        step=0.001
    )

    solidity = st.number_input(
        "Solidity",
        min_value=0.0,
        max_value=1.0,
        value=0.989,
        step=0.001
    )

    roundness = st.number_input(
        "roundness",
        min_value=0.0,
        max_value=1.0,
        value=0.958,
        step=0.001
    )

    compactness = st.number_input(
        "Compactness",
        min_value=0.0,
        max_value=1.0,
        value=0.913,
        step=0.001
    )

# ============================================================
# COLUMN 4
# ============================================================

with col4:

    shape_factor1 = st.number_input(
        "ShapeFactor1",
        min_value=0.0,
        value=0.00733,
        step=0.00001,
        format="%.5f"
    )

    shape_factor2 = st.number_input(
        "ShapeFactor2",
        min_value=0.0,
        value=0.00315,
        step=0.00001,
        format="%.5f"
    )

    shape_factor3 = st.number_input(
        "ShapeFactor3",
        min_value=0.0,
        value=0.834,
        step=0.001
    )

    shape_factor4 = st.number_input(
        "ShapeFactor4",
        min_value=0.0,
        value=0.998,
        step=0.001
    )

# ============================================================
# CREATE INPUT DATAFRAME
# ============================================================

input_data = pd.DataFrame(
    [[
        area,
        perimeter,
        major_axis,
        minor_axis,
        aspect_ratio,
        eccentricity,
        convex_area,
        equiv_diameter,
        extent,
        solidity,
        roundness,
        compactness,
        shape_factor1,
        shape_factor2,
        shape_factor3,
        shape_factor4
    ]],
    columns=features
)

# ============================================================
# SHOW INPUT
# ============================================================

with st.expander("View Input Data"):
    st.dataframe(
        input_data,
        use_container_width=True
    )

# ============================================================
# PREDICTION
# ============================================================

st.divider()

if st.button(
    "🔮 Predict Bean Variety",
    type="primary",
    use_container_width=True
):

    try:

        # Predict class
        prediction = model.predict(input_data)

        predicted_class = prediction[0]

        st.success(
            f"Predicted Dry Bean Variety: {predicted_class}"
        )

        # ====================================================
        # PROBABILITIES
        # ====================================================

        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(input_data)[0]

            classes = model.classes_

            probability_df = pd.DataFrame({
                "Bean Variety": classes,
                "Probability": probabilities
            })

            probability_df["Probability (%)"] = (
                probability_df["Probability"] * 100
            )

            probability_df = probability_df.sort_values(
                by="Probability",
                ascending=False
            )

            st.subheader("Prediction Probabilities")

            display_df = probability_df[
                ["Bean Variety", "Probability (%)"]
            ].copy()

            display_df["Probability (%)"] = (
                display_df["Probability (%)"].round(2)
            )

            st.dataframe(
                display_df,
                use_container_width=True
            )

            # =================================================
            # BAR CHART
            # =================================================

            st.subheader("Probability Distribution")

            chart_data = probability_df.set_index(
                "Bean Variety"
            )["Probability (%)"]

            st.bar_chart(chart_data)

        else:
            st.info(
                "This model does not support prediction probabilities."
            )

        # ====================================================
        # RESULT SUMMARY
        # ====================================================

        st.subheader("Prediction Summary")

        result_df = input_data.copy()

        result_df["Predicted_Class"] = predicted_class

        st.dataframe(
            result_df,
            use_container_width=True
        )

    except Exception as e:

        st.error("Prediction failed.")

        st.exception(e)

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Multi-Class Dry Bean Classification Using Machine Learning"
)