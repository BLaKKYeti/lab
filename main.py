from kernel.runtime import Runtime


def main():

    system = Runtime()

    system.start()

    result = system.execute(
        "filesystem",
        "list_pdfs"
    )

    print("PDF Results:")
    print(result)


if __name__ == "__main__":
    main()