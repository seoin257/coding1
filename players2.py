import streamlit as st

st.markdown("""
<style>
.big-btn button {
    width: 100%;
    height: 100px;
    font-size: 32px;
    font-weight: bold;
}
.trust button {
    background-color: #1f77ff;
    color: white;
}
.betray button {
    background-color: #ff3b3b;
    color: white;
}
</style>
""", unsafe_allow_html=True)

if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.p = [None, None]
    st.session_state.score = [0, 0]

def reset_game():
    st.session_state.step = 1
    st.session_state.p = [None, None]
    st.session_state.score = [0, 0]
    st.rerun()

st.title("2인 죄수의 딜레마")

if st.button("리셋"):
    reset_game()

# ===== 선택 단계 =====
if st.session_state.step <= 2:
    idx = st.session_state.step - 1
    st.subheader(f"Player {idx+1} 선택")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="big-btn trust">', unsafe_allow_html=True)
        if st.button("신뢰", key=f"trust_{idx}"):
            st.session_state.p[idx] = "C"
            st.session_state.step += 1
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="big-btn betray">', unsafe_allow_html=True)
        if st.button("배신", key=f"betray_{idx}"):
            st.session_state.p[idx] = "D"
            st.session_state.step += 1
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ===== 결과 =====
elif st.session_state.step == 3:
    p1, p2 = st.session_state.p

    if p1 == "C" and p2 == "C":
        s = [3, 3]
    elif p1 == "D" and p2 == "C":
        s = [5, -1]
    elif p1 == "C" and p2 == "D":
        s = [-1, 5]
    else: # D D
        s = [0, 0]

    for i in range(2):
        st.session_state.score[i] += s[i]

    st.subheader("결과")
    for i in range(2):
        st.write(
            f"Player {i+1}: "
            f"{'신뢰' if st.session_state.p[i]=='C' else '배신'} ({s[i]:+d})"
        )
