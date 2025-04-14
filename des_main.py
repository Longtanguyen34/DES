from des_lib import encrypt, decrypt

def read_input_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def write_output_file(file_path, data, is_binary=False):
    mode = 'wb' if is_binary else 'w'
    with open(file_path, mode) as f:
        f.write(data if not is_binary else data)

def main():
    key = "8bytekey"  # DES chỉ chấp nhận khóa dài đúng 8 byte

    # Đọc dữ liệu đầu vào
    plain_text = read_input_file('input.txt')

    # Mã hoá
    encrypted = encrypt(plain_text, key)
    write_output_file('encrypted.txt', encrypted, is_binary=True)

    # Giải mã
    decrypted = decrypt(encrypted, key)
    write_output_file('decrypted.txt', decrypted)

if __name__ == '__main__':
    main()
