import streamlit as st
import random

st.set_page_config(page_title="A Reminder: I Adore You, Lucy 💗")

st.title("💞 For You, My Lucy 💞")
st.write("Click the button whenever you need a little reminder of how much I adore you.")

reminders = [
    """You know, sometimes I think you are one the few good things that god sent me in this life.  
I am an atheist and you know that, but sometimes, you make me want to believe in something.  
  
You make me want to become one of those people who go to church on Sundays and drink tea in the mornings.  
Who go on walks and appreciate nature.  
  
I see everything black and white, yet you make me want to explore the grey area.  
  
For you, I would convert.""",

    """The quietness that I hated — until you taught me it was okay.  
Always feeling panicked and a bit scared.  
Yet you sat with me in silence, and I learned calm could be kind.  
  
You taught me that softness doesn’t mean weakness.  
I do not believe in fate, yet you sat on the same train as me.  
A train that had no direction until you appeared in the seat next to me.  
  
I thought I had to fly without a seatbelt to feel alive —  
but realizing that sitting under a tree, quietly observing the scenery and watching the world breathe,  
is the best feeling there is.""",

    """For you, I’d slow down.  
For you, I’d listen to songs I don’t even like if it makes you smile.  
For you, I’d unlearn my cynicism.""",

    """“Růže mé zahrady, jak dlouhého čekání než si budu moci přičuchnout vaší vůně.”  
řekla, kdysi jedna až po uši zamilovaná holka — je trošku teplá ngl fr smh"""
]

if st.button("Remind Me"):
    st.info(random.choice(reminders))
