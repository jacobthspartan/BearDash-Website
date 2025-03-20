# Welcome to the brain of the website alot of stuff that i dont fully understand LMAO
# i do like this new website my old website for this was a fucking google site that looked like a 2 year old made it Ha Ha
# If you get lost i added chapters for everything that i did if you even get lost it more for me honestly as sometimes i cant even see what the hell im doing
# And without further ado my code!

import streamlit as st


# Add Header and subheader (no shit)
st.header("**Welcome to the official :rainbow[Beardash] website!**")
st.subheader("The *100% best texture pack for Geometry Dash!*")

# Add the download button
if st.button("Download Beardash 6.0! (**GD 2.1 and Windows only!**)"):
    with st.spinner("Preparing your download..."):
        st.success("Click the link below to download!")
        st.markdown("[Download Beardash 6.0](https://drive.google.com/file/d/1FC5JdMbT-UfSP67sOE_htzmveuV2kCy0/view?pli=1)", unsafe_allow_html=True)

# Add a Help link to downgrade to 2.1
st.markdown("If you need help downgrading to Geometry Dash 2.1, click [here](https://www.youtube.com/watch?v=YaW_1kD-WKA).")

#  Add requirments expander
with st.expander(":rainbow[**Requirements**]"):
    st.write("- **Windows 7 or newer**")
    st.write("- **Geometry Dash 2.1**")
    st.write("- **A brain**")
    st.write("- **A computer**")

st.markdown("---")

# Add Indevelopment
st.warning("This website is still in development! So you might see some errors!")

# Add changelog
st.subheader("Changelog")
st.markdown("### Version 6.0")
st.markdown("- Added new icons")
st.markdown("- Added new backgrounds")

st.markdown("---")

# Add Q&A section
st.subheader("Frequently Asked Questions (FAQ)")

with st.expander("Q: Is BearDash paid?"):
    st.write("A: No, it's a free mod.")

with st.expander("Q: Is BearDash done?"):
    st.write("A: No, it's far from finished.")

with st.expander("Q: When will BearDash be finished?"):
    st.write("A: As far as we know, not now, but our beta is being worked on.")

with st.expander("Q: Does BearDash need Geometry Dash?"):
    st.write("A: Yes, without it the textures will be useless.")

with st.expander("Q: Does BearDash get every texture?"):
    st.write("A: No, sadly there's only one person working on textures, one working on the site, and one beta testing.")

with st.expander("Q: Will BearDash be finished?"):
    st.write("A: Maybe, depending on how we feel about this.")

with st.expander("Q: Will this be your only mod?"):
    st.write("A: Again, maybe :)")

# Add an info expander
with st.expander("ℹ️ More Info"):
    st.info(
        """
        Welcome to the new and improved BearDash website, now hosted on **Streamlit**! 
        Streamlit allows us to create interactive and user-friendly web apps with ease. 
        You can learn more about Streamlit [here](https://streamlit.io).

        And ofc this is all for jokes this is not the best texture pack for gd but your already new that :)

        **BearDash** is a free texture pack for Geometry Dash, designed to enhance your gaming experience. 
        Please note that this project is still in development, and we appreciate your patience and support.

        If you encounter any issues or have suggestions, feel free to leave your feedback below. 
        Thank you for being part of our journey! ❤️
        """
    )

st.markdown("---")

# add feedback
st.subheader("Feedback")
feedback = st.text_area("Please leave your feedback here (bugs, suggestions, etc.) we really appresaite it! ❤️")
if st.button("Submit"):
    st.success("Thank you for your feedback ❤️")


#add a super fucking long error for no reason but why not
st.error("THIS ONLY WORKS ON GD 2.11 AND NOT ON GD 2.2 WE ARE A SMALL TEAM AND ARE WORKING ON IT I LOST MY HARD DRIVE SO I HAVE TO RECREATE THE WHOLE TEXTURE PACK THE TEXTERPACK FOR 2.2 I DONT KNOW WHEN IT WILL BE DONE BUT I WILL TRY TO MAKE IT AS FAST AS POSSIBLE")

# Add the footer
st.markdown(
    """
    ---
        Made with ❤️ by Jacob
        """
    )
