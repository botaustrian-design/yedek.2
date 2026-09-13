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

    bind(server_fd, (struct sockaddr*)&address, sizeof(address));
    listen(server_fd, 5);

    std::cout << "Sunucu calisiyor: http://localhost:5000" << std::endl;

    while (true) {
        int new_socket = accept(server_fd, NULL, NULL);
        if (new_socket < 0) continue;

        char buffer[1024] = {0};
        read(new_socket, buffer, 1024);

        // HTML renkli yazi kodlari
        std::string html = 
            "<!DOCTYPE html><html><head><meta charset='UTF-8'></head>"
            "<body style='background:#111; color:white; font-family:sans-serif; padding:20px;'>"
            "  <h1 style='color:red;'>Kırmızı Yazı</h1>"
            "  <h2 style='color:lime;'>Yeşil Yazı</h2>"
            "  <h3 style='color:cyan;'>Mavi Yazı</h3>"
            "  <p style='color:yellow; font-size:20px;'>Sarı Yazı</p>"
            "  <p style='color:#ff00ff;'>Pembe / Magenta Yazı (#ff00ff)</p>"
            "  <p style='background:orange; color:black; padding:10px;'>Turuncu Arka Planlı Siyah Yazı</p>"
            "</body></html>";

        std::string response = 
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=UTF-8\r\n"
            "Content-Length: " + std::to_string(html.length()) + "\r\n"
            "Connection: close\r\n\r\n" + html;

        send(new_socket, response.c_str(), response.length(), 0);
        close(new_socket);
    }
    return 0;
}
