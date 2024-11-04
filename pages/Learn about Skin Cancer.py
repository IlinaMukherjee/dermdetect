import streamlit as st
from streamlit_lottie import st_lottie 
import pandas as pd
import numpy as np


tab1, tab2, tab3 = st.tabs(["What happens in skin cancer?", "Types of Skin Cancer","Symptoms"])
with tab1:
    st.title('What happens in Skin Cancer?')
    st.subheader('Skin cancer is a disease where some of the body’s skin cells grow uncontrollably and spread to other parts of the body.')
    st.write(" ")
    st.write('**This type of cancer can start almost anywhere on the skin, making it a significant concern given that the skin is the body’s largest organ.**')
    st.write(" ")
    st.markdown('Skin cancer results from mutations in the DNA of skin cells, which leads to rapid cell division and tumor formation. Tumors can be _:blue[**benign (non-cancerous) or malignant (cancerous), with malignant tumors having the potential to spread to other parts of the body.**]_')
    st.write(" ")
    st.image("cancerd1.jpg", caption='source: cancer.gov')
    st.divider()
    st.header("How does Skin Cancer develop?")
    st.subheader(":blue[Cancer is a genetic disease: it is caused by changes in genes that control cell growth and division.]")
    st.subheader("Causes of Genetic Changes: ")
    st.write("o	**Cell Division Errors:** Mistakes during cell replication.")
    st.write("o	**Environmental Damage:** Harmful substances like tobacco smoke and UV rays.")
    st.write(" o **Inherited Mutations**: Genetic predispositions passed from parents.")
    st.write("*The body's ability to eliminate damaged DNA decreases with age, increasing cancer risk.*")
    st.write("Each cancer has a unique combination of genetic changes, which can vary within the same tumor.")
    st.subheader(":blue[Cancer is typically caused by genetic alterations in these three gene types: proto-oncogenes, DNA repair genes and tumor supressor genes. ]")
    st.write("These genes are concerned with normal cell division, cell growth and fixing damaged DNA. Cells with mutations in these genes tend to develop additional mutations in other genes and changes in their chromosomes, such as duplications and deletions of chromosome parts. Together, these mutations may cause the cells to become cancerous. ")
    st.image("cancerd2.png", caption='cclg.org.uk')
    st.divider()
    st.subheader("What happens in Cancer Cells?")
    df = pd.DataFrame(
    [
        {"Feature": "Uncontrolled Growth", "What happens?": "Cancer cells grow without signals, unlike normal cells."},
        {"Feature": "Ignoring Apoptosis", "What happens?": "Cancer cells avoid signals to stop dividing or die."},
        {"Feature": "Invasion and Spread", "What happens?": "Cancer cells invade nearby areas and spread; normal cells do not."},
        {"Feature": "Immune System Evasion", "What happens?": "Cancer cells hide from and trick the immune system to support their growth."},
        {"Feature": "Genetic Changes", "What happens?": "Cancer cells accumulate chromosomal changes and often have double the normal number of chromosomes."},
        {"Feature": "Nutrient Use", "What happens?": "Cancer cells use different nutrients and make energy differently, aiding rapid growth."},
        {"Feature": "Therapeutic Targets", "What happens?": "Treatments exploit cancer cells’ unique features, such as preventing blood vessel growth to tumors."}
    ]
    )
    st.dataframe(df, use_container_width=True)

with tab2:
    st.title("Types of Skin Cancer")
    st.subheader(":blue[There are several types of skin cancer, but the most common ones include basal cell carcinoma (BCC), squamous cell carcinoma (SCC), and melanoma.]")
    st.markdown(
        """

            - **Basal Cell Carcinoma (BCC)**:     This is the most common form of skin cancer. BCC arises from the basal cells in the epidermis, the skin’s outermost layer. It often appears as a painless, raised area of skin that may be shiny or pearly in appearance. BCC grows slowly and rarely metastasizes (spreads to other parts of the body), but if left untreated, it can cause significant local damage.
            - **Squamous Cell Carcinoma (SCC)**:     SCC originates from squamous cells, which are flat cells located just below the outer surface of the skin. SCC is more likely than BCC to invade deeper layers of skin and spread to other parts of the body. It typically appears as a red, scaly, or crusted lesion and can be found on sun-exposed areas such as the face, ears, and hands.
            - **Melanoma**:       Melanoma is the most dangerous form of skin cancer, arising from melanocytes, the cells that produce pigment (melanin). Melanomas can develop in existing moles or appear as new dark spots on the skin. They are known for their ability to spread rapidly to other parts of the body if not detected early.


        """
    )
    st.image("cancerd3.jpg")
    st.divider()
    st.subheader("Some Data")
    col1,col2 = st.columns(2)
    with col1:
        st.write("**The most common histological type of skin cancer is Basal Cell Carcinoma (BCC) ~ 80% followed by Squamous Cell Carcinoma (SCC) ~ 17% , Melanoma & Merkel Cell Carcinoma (MCC) ~ 3% (the last 2 are deadliest one amongst the 4).**")
    with col2:
        st.image("cancerd4.jpg")
    st.divider()

with tab3:
    st.title("Symptoms and Stages of Skin Cancer")
    st.subheader(":blue[The most common symptom of skin cancer is skin lesions. Skin lesions looks different depending on what type of skin cancer you have. The ABCDE rule tells you what signs to watch for:]")
    st.markdown(
        """

         - **A**symmetry: Irregular shape.
         - **B**order: Blurry or irregularly shaped edges.
         - **C**olor: Mole with more than one color.
         - **D**iameter: Larger than a pencil eraser (6 millimeters).
         - **E**volution: Enlarging, changing in shape, color or size. 


        """
    )
    st.caption("Source: cancer.org")
    st.image("cancerd5.png", caption='Source: ISIC Dataset')
    st.divider()
