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
    st.session_state.p = [None, None, None]
    st.session_state.score = [0, 0, 0]

def reset_game():
    st.session_state.step = 1
    st.session_state.p = [None, None, None]
    st.session_state.score = [0, 0, 0]
    st.rerun()

st.title("3인 죄수의 딜레마")

# 초기화 버튼
if st.button("리"):
    reset_game()

# ===== 선택 단계 =====
if st.session_state.step <= 3:
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
elif st.session_state.step == 4:
    p = st.session_state.p
    d = p.count("D")

    if d == 0:        # C C C
        s = [3, 3, 3]
    elif d == 1:      # D C C
        s = [5 if x=="D" else 0 for x in p]
    elif d == 2:      # D D C
        s = [4 if x=="D" else -1 for x in p]
    else:             # D D D
        s = [0, 0, 0]

    for i in range(3):
        st.session_state.score[i] += s[i]

    st.subheader("결과")
    for i in range(3):
        st.write(
            f"Player {i+1}: "
            f"{'신뢰' if p[i]=='C' else '배신'} ({s[i]:+d})"
        )

    st.write("---")
