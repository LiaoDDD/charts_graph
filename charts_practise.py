import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import rcParams


# 設置支持中文的字體
rcParams['font.sans-serif'] = ['Arial Unicode Ms']  # 使用黑體 (SimHei)
rcParams['axes.unicode_minus'] = False    # 解決負號顯示問題

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Create flowchart shapes using rectangles
ax.text(0.5, 0.9, "需求分析", ha='center', va='center', fontsize=12, bbox=dict(boxstyle='round', facecolor='lightblue'))
ax.text(0.5, 0.75, '技術選擇與環境設置', ha='center', va='center', fontsize=12, bbox=dict(boxstyle='round', facecolor='lightgreen'))
ax.text(0.5, 0.6, '資料庫構建', ha='center', va='center', fontsize=12, bbox=dict(boxstyle='round', facecolor='lightyellow'))
ax.text(0.5, 0.45, '系統開發', ha='center', va='center', fontsize=12, bbox=dict(boxstyle='round', facecolor='lightpink'))
ax.text(0.5, 0.3, '系統測試與優化', ha='center', va='center', fontsize=12, bbox=dict(boxstyle='round', facecolor='lightcoral'))
ax.text(0.5, 0.15, '基線系統測試', ha='center', va='center', fontsize=12, bbox=dict(boxstyle='round', facecolor='lavender'))
ax.text(0.5, 0.0, 'RAG增強系統測試與評估', ha='center', va='center', fontsize=12, bbox=dict(boxstyle='round', facecolor='lightgray'))

# Draw arrows
ax.annotate('', xy=(0.5, 0.82), xytext=(0.5, 0.88), arrowprops=dict(arrowstyle='->'))
ax.annotate('', xy=(0.5, 0.67), xytext=(0.5, 0.73), arrowprops=dict(arrowstyle='->'))
ax.annotate('', xy=(0.5, 0.52), xytext=(0.5, 0.58), arrowprops=dict(arrowstyle='->'))
ax.annotate('', xy=(0.5, 0.37), xytext=(0.5, 0.43), arrowprops=dict(arrowstyle='->'))
ax.annotate('', xy=(0.5, 0.22), xytext=(0.5, 0.28), arrowprops=dict(arrowstyle='->'))
ax.annotate('', xy=(0.5, 0.07), xytext=(0.5, 0.13), arrowprops=dict(arrowstyle='->'))

# Hide axes
ax.axis('off')

# Display the flowchart
plt.title('研究設計與步驟流程圖', fontsize=14)
plt.show()