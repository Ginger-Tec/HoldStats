import pandas as pd
import streamlit as st

# Initialize the DataFrame to store hand information and HUD metrics
if 'hand_history' not in st.session_state:
    st.session_state.hand_history = pd.DataFrame(columns=['fold', 'limp_call', 'cold_call', 'open_raise', '3bet_raise', 'VPIP', 'PFR', '3Bet'])


def self_pre_hud():
    st.title("Self Preflop HUD")

    col_1 = st.columns([1, 1, 1, 1, 1])

    fold = col_1[0].button("Fold", key="fold", use_container_width=True)
    limp_call = col_1[1].button("Limp Call", key="limp_call", use_container_width=True)
    cold_call = col_1[2].button("Cold Call", key="cold_call", use_container_width=True)
    open_raise = col_1[3].button("Open Raise", key="open_raise", use_container_width=True)
    three_bet_raise = col_1[4].button("3bet Raise", key="3bet_raise", use_container_width=True)

    # Update the DataFrame based on button clicks
    if any([fold, limp_call, cold_call, open_raise, three_bet_raise]):
        new_hand = pd.DataFrame([{
            'fold': fold,
            'limp_call': limp_call,
            'cold_call': cold_call,
            'open_raise': open_raise,
            '3bet_raise': three_bet_raise
        }])

        st.session_state.hand_history = pd.concat([st.session_state.hand_history, new_hand], ignore_index=True)

        # Calculate the HUD statistics based on historical data
        hand_count = len(st.session_state.hand_history)
        if hand_count > 0:
            vpip = (st.session_state.hand_history[['limp_call', 'cold_call', 'open_raise', '3bet_raise']].sum().sum()) / hand_count
            pfr = st.session_state.hand_history['open_raise'].sum() / hand_count
            three_bet = st.session_state.hand_history['3bet_raise'].sum() / hand_count

            # Add VPIP, PFR, and 3Bet to the DataFrame
            st.session_state.hand_history.at[hand_count - 1, 'VPIP'] = vpip * 100
            st.session_state.hand_history.at[hand_count - 1, 'PFR'] = pfr * 100
            st.session_state.hand_history.at[hand_count - 1, '3Bet'] = three_bet * 100

    # st.write(st.session_state.hand_history)

    # Display the current HUD metrics
    hand_count = len(st.session_state.hand_history)
    if hand_count > 0:
        vpip = st.session_state.hand_history['VPIP'].iloc[-1]
        pfr = st.session_state.hand_history['PFR'].iloc[-1]
        three_bet = st.session_state.hand_history['3Bet'].iloc[-1]

        df_hud = pd.DataFrame(data=[vpip, pfr, three_bet], index=['VPIP', 'PFR', '3Bet'], columns=['HUD'])

        st.data_editor(df_hud, use_container_width=True,
                       column_config={'HUD': st.column_config.ProgressColumn('HUD', min_value=0, max_value=100, format='%.2f%%')})

        # Optionally, plot the historical data to visualize changes over time
        st.line_chart(st.session_state.hand_history[['VPIP', 'PFR', '3Bet']])

    with st.expander("Show Hand History"):
        df_hand_history = st.session_state.hand_history.copy()
        # 정렬
        df_hand_history = df_hand_history.sort_index(ascending=False)
        st.dataframe(df_hand_history)
