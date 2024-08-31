import streamlit as st

from page.hold_stats import hold_stats
from page.self_hud import self_hud

pages = {
    "hold'em": [
        st.Page(hold_stats, title="Hold Stats", icon="🎰"),
        st.Page(self_hud, title="SELF HUD", icon="🃏"),
    ],
}

pg = st.navigation(pages)
pg.run()
