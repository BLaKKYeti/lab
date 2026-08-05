from kernel.runtime import Runtime


os = Runtime()

os.start()

result = os.execute(
    "filesystem",
    "list_pdfs"
)

print("\nPDF Results:")
for pdf in result:
    print(pdf)