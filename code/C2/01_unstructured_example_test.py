#from unstructured.partition.auto import partition
#使用 unstructured.partition.pdf.partition_pdf 代替 unstructured.partition.auto.partition
from unstructured.partition.pdf import partition_pdf

# PDF文件路径
pdf_path = "../../data/C2/pdf/rag.pdf"

# 使用Unstructured加载并解析PDF文档
elements = partition_pdf(
    filename=pdf_path,
    content_type="application/pdf",
    strategy="ocr_only",
    languages=["chi_sim"]
)

# 打印解析结果
print(f"解析完成: {len(elements)} 个元素, {sum(len(str(e)) for e in elements)} 字符")

# 统计元素类型
from collections import Counter
types = Counter(e.category for e in elements)
print(f"元素类型: {dict(types)}")

# 显示所有元素
print("\n所有元素:")
for i, element in enumerate(elements, 1):
    print(f"Element {i} ({element.category}):")
    print(element)
    print("=" * 60)


'''
hi_res结果：
解析完成: 221 个元素, 8265 字符
元素类型: {'Image': 22, 'UncategorizedText': 85, 'Header': 4, 'NarrativeText': 68, 'Table': 4, 'FigureCaption': 4, 'Title': 30, 'ListItem': 4}
ocr_only结果：
解析完成: 103 个元素, 2122 字符
元素类型: {'Title': 72, 'UncategorizedText': 26, 'NarrativeText': 5}
'''
