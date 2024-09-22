age = 28
intensity = "high"

if intensity == "low":
    rate = 0.5
elif intensity == "moderate":
    rate = 0.7
else:
    rate = 0.85
    
BPM = (220 - age) * rate

print(f'목표 BPM은 {BPM}입니다')