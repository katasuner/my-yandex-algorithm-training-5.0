p, v = (int(num) for num in input().split())
q, m = (int(num) for num in input().split())

v_start, v_end = p - v, p + v
m_start, m_end = q - m, q + m

overlap = max(0, ((min(v_end, m_end)) - (max(v_start, m_start)) + 1))

print((v_end - v_start + 1) + (m_end - m_start + 1) - overlap)