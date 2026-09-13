#include <iostream>
#include <cstring>
#include <string>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

int main() {
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    int opt = 1;
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    sockaddr_in address;
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(5000);

    if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) {
        std::cout << "Hata: Port mesgul! 'pkill -f dosya2' yazin." << std::endl;
        return 1;
    }

    listen(server_fd, 3);
    std::cout << "Sunucu calisiyor: http://localhost:5000" << std::endl;

    while (true) {
        int new_socket = accept(server_fd, NULL, NULL);
        if (new_socket < 0) continue;

        char buffer[1024] = {0};
        recv(new_socket, buffer, 1024, 0);

        // LOGOLU HTML İÇERİĞİ
        std::string body = 
            "<!DOCTYPE html>"
            "<html>"
            "<head><meta charset='utf-8'><title>Logolu C++ Sitem</title></head>"
            "<body style='background-color:#121212; color:#ffffff; font-family:sans-serif; text-align:center; padding-top:40px;'>"
            
            "  <!-- LOGO (İnternet Adresinden) -->"
            "  <img src='https://upload.wikimedia.org/wikipedia/commons/1/18/ISO_C%2B%2B_Logo.svg' width='120' style='margin-bottom:20px;'><br>"

            "  <h1>Logolu C++ Siteniz Yayında!</h1>"
            "  <p>1. Satır: Logo başarıyla eklendi.</p>"
            "  <p>2. Satır: Resim linkini değiştirerek istediğiniz logoyu koyabilirsiniz.</p>"
            "</body>"
            "</html>";

        std::string response = 
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            "Content-Length: " + std::to_string(body.length()) + "\r\n"
            "Connection: close\r\n\r\n" + body;

        send(new_socket, response.c_str(), response.length(), 0);
        close(new_socket);
    }
    return 0;
}

