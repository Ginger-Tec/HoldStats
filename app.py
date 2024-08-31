import streamlit as st

from page.hold_stats import hold_stats
from page.self_hud import self_hud
from page.self_pre_hud import self_pre_hud

pages = {
    "hold'em": [
        st.Page(hold_stats, title="Hold Stats", icon="⏯️"),
        st.Page(self_pre_hud, title="Self Pre HUD", icon="✏️"),
    ],
}

pg = st.navigation(pages)
pg.run()
