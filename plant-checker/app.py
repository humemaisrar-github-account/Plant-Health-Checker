import streamlit as st
from typing import List

 
# Plant Model & Manager
class Plant:
    def __init__(self, name: str, description: str, common_issues: List[str]):
        self.name = name
        self.description = description
        self.common_issues = common_issues

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "common_issues": self.common_issues
        }

class PlantManager:
    def __init__(self):
        # Expanded plant database
        self.plants = [
            Plant("Rose", "A beautiful flowering plant, popular for its fragrant flowers and thorny stems.", 
                  ["Powdery mildew", "Aphids", "Black spot", "Rust fungus"]),
            Plant("Tulip", "A spring-blooming flower, known for its bright and colorful petals.",
                  ["Bulb rot", "Gray mold", "Aphid infestation"]),
            Plant("Tomato", "A commonly grown vegetable plant used in many dishes worldwide.",
                  ["Blight", "Leaf curl", "Early blight", "Tomato hornworm"]),
            Plant("Sunflower", "Tall plants known for large yellow flowers that follow the sun.",
                  ["Downy mildew", "Rust", "Aphids", "Sclerotinia wilt"]),
            Plant("Basil", "A fragrant herb used in cooking, especially in Italian cuisine.",
                  ["Fusarium wilt", "Downy mildew", "Root rot"]),
            Plant("Cactus", "Succulent plants that store water, ideal for dry conditions.",
                  ["Root rot", "Mealybugs", "Spider mites"]),
            Plant("Mint", "A refreshing herb with aromatic leaves used in drinks and dishes.",
                  ["Rust", "Powdery mildew", "Verticillium wilt"]),
            Plant("Orchid", "Elegant flowering plants with delicate blooms, often kept indoors.",
                  ["Root rot", "Scale insects", "Leaf spot"]),
            Plant("Lavender", "Fragrant purple flower known for calming scent and essential oils.",
                  ["Root rot", "Shab disease", "Crown rot"]),
            Plant("Peach", "Fruit tree that produces sweet juicy peaches.",
                  ["Peach leaf curl", "Brown rot", "Aphids"]),
        ]

    def find_plant(self, name: str):
        name = name.strip().lower()
        for plant in self.plants:
            if plant.name.lower() == name:
                return plant
        return None

 
# Streamlit UI
 

st.set_page_config(page_title="Plant Care Assistant 🌿", page_icon="🌱")

st.title("🌿 Plant Care Assistant")
st.markdown("Write the plant name and upload its image to get basic info and common problems.")

# Plant manager instance
manager = PlantManager()

# Input plant name
plant_name = st.text_input("Enter Plant Name (e.g., Rose, Tomato):")

# Upload plant image
uploaded_image = st.file_uploader("Upload a plant image (optional):", type=["png", "jpg", "jpeg"])

# Button to search plant info
if st.button("Get Plant Info"):

    if not plant_name.strip():
        st.warning("Please enter a plant name.")
    else:
        plant = manager.find_plant(plant_name)
        if plant:
            st.success(f"Information about **{plant.name}**:")
            st.write(plant.description)

            st.markdown("### Common Issues / Diseases")
            for issue in plant.common_issues:
                st.write(f"• {issue}")

            if uploaded_image:
                st.image(uploaded_image, caption=f"{plant.name} Image", use_container_width=True)
                st.info("Image uploaded successfully! (AI analysis coming soon...)")
            else:
                st.info("You can upload an image to help analyze the plant condition (feature coming soon).")
        else:
            st.error(f"Sorry, we have no information about '{plant_name}'. Please try another plant name.")

# Footer / Credits
st.markdown("---")
st.markdown("Developed with ❤️ using Python, Streamlit, and OOP principles.")
st.markdown("Created by Humema 🌸")
st.markdown("Your friendly Plant Care Assistant 🌿")
