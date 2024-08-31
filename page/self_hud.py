import streamlit as st

hand_info = {
    'fold': 0,
    'limp_call': 0,  # 림프콜(Big Blind 만큼 Call)
    'cold_call': 0,  # 콜드콜(raised pot 에 콜)
    'open_raise': 0,  # 오픈 레이즈(최초 베팅)
    '3bet_raise': 0,  # 3벳 레이즈(raised pot 에 레이즈)

}


def self_hud():
    st.title("Self Preflop HUD")

    col_1 = st.columns([1, 1, 1, 1, 1])

    hand_info['fold'] += col_1[0].button("Fold", key="fold", use_container_width=True)
    hand_info['limp_call'] += col_1[1].button("Limp Call", key="limp_call", use_container_width=True)
    hand_info['cold_call'] += col_1[2].button("Cold Call", key="cold_call", use_container_width=True)
    hand_info['open_raise'] += col_1[3].button("Open Raise", key="open_raise", use_container_width=True)
    hand_info['3bet_raise'] += col_1[4].button("3bet Raise", key="3bet_raise", use_container_width=True)

    st.write(hand_info)

    # VPIP = (Call + Raise) / (Call + Raise + Fold)
    # PFR = Raise / (Call + Raise + Fold)
    # 3Bet = 3Bet / (Call + Raise + Fold)

    hand_count = sum(hand_info.values())
    # zero division error
    if hand_count == 0:
        return
    vpip = (hand_info['limp_call'] + hand_info['cold_call'] + hand_info['open_raise'] + hand_info['3bet_raise']) / hand_count
    pfr = hand_info['open_raise'] / hand_count
    three_bet = hand_info['3bet_raise'] / hand_count

    st.metric("VPIP", f"{vpip*100:.2f}%")
    st.metric("PFR", f"{pfr*100:.2f}%")
    st.metric("3Bet", f"{three_bet*100:.2f}%")
