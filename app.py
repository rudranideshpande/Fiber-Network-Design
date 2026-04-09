import streamlit as st
import subprocess

st.title("Fiber Network Design (Kruskal MST)")

n = st.number_input("Number of vertices", min_value=1)
e = st.number_input("Number of edges", min_value=1)

edges = []

for i in range(int(e)):
    u = st.number_input(f"Edge {i} - u", key=f"u{i}")
    v = st.number_input(f"Edge {i} - v", key=f"v{i}")
    w = st.number_input(f"Edge {i} - weight", key=f"w{i}")
    edges.append((u, v, w))

if st.button("Run Algorithm"):
    input_data = f"{n} {e}\n"
    for edge in edges:
        input_data += f"{edge[0]} {edge[1]} {edge[2]}\n"

    result = subprocess.run(
        ["./kruskal"],   # use "kruskal.exe" on Windows
        input=input_data,
        text=True,
        capture_output=True
    )

    st.text(result.stdout)