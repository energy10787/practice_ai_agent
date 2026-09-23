from functions.get_files_info import get_files_info

def test_get_files_info() -> None:
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)

    result = get_files_info("calculator", "main.py")
    print("Result for 'main.py':")
    print(result)

    result = get_files_info("calculator", "pkg")
    print("Results for 'pkg")
    print(result)  

if __name__ == "__main__":
    test_get_files_info()

