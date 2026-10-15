/**
 * C++ HTTP Web Server (Windows Winsock2)
 * Melayani index.html, file CSS, JS, Gambar, dan SVG secara lokal.
 *
 * Kompilasi:
 *   g++ -O2 server.cpp -o server.exe -lws2_32
 *
 * Jalankan:
 *   .\server.exe
 * Buka di browser: http://localhost:8080
 */

#include <winsock2.h>
#include <ws2tcpip.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>

#pragma comment(lib, "ws2_32.lib")

std::string getMimeType(const std::string& path) {
    size_t dotPos = path.rfind('.');
    if (dotPos == std::string::npos) return "application/octet-stream";
    std::string ext = path.substr(dotPos);
    std::transform(ext.begin(), ext.end(), ext.begin(), ::tolower);

    if (ext == ".html" || ext == ".htm") return "text/html; charset=utf-8";
    if (ext == ".css") return "text/css; charset=utf-8";
    if (ext == ".js") return "application/javascript; charset=utf-8";
    if (ext == ".json") return "application/json";
    if (ext == ".png") return "image/png";
    if (ext == ".jpg" || ext == ".jpeg") return "image/jpeg";
    if (ext == ".gif") return "image/gif";
    if (ext == ".svg") return "image/svg+xml";
    if (ext == ".webp") return "image/webp";
    if (ext == ".ico") return "image/x-icon";
    if (ext == ".woff") return "font/woff";
    if (ext == ".woff2") return "font/woff2";
    if (ext == ".ttf") return "font/ttf";
    return "application/octet-stream";
}

bool fileExists(const std::string& path) {
    std::ifstream file(path.c_str(), std::ios::in | std::ios::binary);
    return file.good();
}

std::string readFileBinary(const std::string& filepath) {
    std::ifstream file(filepath.c_str(), std::ios::in | std::ios::binary);
    if (!file.is_open()) return "";
    std::ostringstream ss;
    ss << file.rdbuf();
    return ss.str();
}

int main() {
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "WSAStartup failed." << std::endl;
        return 1;
    }

    SOCKET listenSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (listenSocket == INVALID_SOCKET) {
        std::cerr << "Error creating socket: " << WSAGetLastError() << std::endl;
        WSACleanup();
        return 1;
    }

    BOOL opt = TRUE;
    setsockopt(listenSocket, SOL_SOCKET, SO_REUSEADDR, (char*)&opt, sizeof(opt));

    sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = INADDR_ANY;
    serverAddr.sin_port = htons(8080);

    if (bind(listenSocket, (sockaddr*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR) {
        std::cerr << "Bind failed with error: " << WSAGetLastError() << std::endl;
        closesocket(listenSocket);
        WSACleanup();
        return 1;
    }

    if (listen(listenSocket, SOMAXCONN) == SOCKET_ERROR) {
        std::cerr << "Listen failed." << std::endl;
        closesocket(listenSocket);
        WSACleanup();
        return 1;
    }

    std::cout << "==========================================================" << std::endl;
    std::cout << " [C++ HTTP Web Server Aktif]" << std::endl;
    std::cout << " URL : http://localhost:8080" << std::endl;
    std::cout << " Web : W3Schools How To Replica 1:1 (Interaktif & Lengkap)" << std::endl;
    std::cout << " Tekan Ctrl+C untuk menghentikan server." << std::endl;
    std::cout << "==========================================================" << std::endl;

    while (true) {
        SOCKET clientSocket = accept(listenSocket, NULL, NULL);
        if (clientSocket == INVALID_SOCKET) {
            continue;
        }

        char buffer[4096] = {0};
        int bytesReceived = recv(clientSocket, buffer, sizeof(buffer) - 1, 0);
        if (bytesReceived > 0) {
            std::string req(buffer);
            size_t firstSpace = req.find(' ');
            size_t secondSpace = req.find(' ', firstSpace + 1);

            std::string path = "/";
            if (firstSpace != std::string::npos && secondSpace != std::string::npos) {
                path = req.substr(firstSpace + 1, secondSpace - firstSpace - 1);
            }

            // Remove query params if any
            size_t qPos = path.find('?');
            if (qPos != std::string::npos) {
                path = path.substr(0, qPos);
            }

            if (path == "/" || path == "/index.html" || path == "/default.asp") {
                path = "index.html";
            } else {
                if (path.length() > 0 && path[0] == '/') {
                    path = path.substr(1);
                }
            }

            // Replace '/' with '\' for Windows filesystem
            std::string localPath = path;
            for (char &c : localPath) {
                if (c == '/') c = '\\';
            }

            // Check if local file exists, otherwise check root filename
            std::string chosenFile = "";
            if (fileExists(localPath)) {
                chosenFile = localPath;
            } else {
                size_t slash = localPath.rfind('\\');
                if (slash != std::string::npos) {
                    std::string baseName = localPath.substr(slash + 1);
                    if (fileExists(baseName)) {
                        chosenFile = baseName;
                    }
                }
            }

            std::string response;
            if (!chosenFile.empty()) {
                std::string content = readFileBinary(chosenFile);
                std::string mime = getMimeType(chosenFile);
                response = "HTTP/1.1 200 OK\r\n"
                           "Content-Type: " + mime + "\r\n"
                           "Content-Length: " + std::to_string(content.size()) + "\r\n"
                           "Access-Control-Allow-Origin: *\r\n"
                           "Connection: close\r\n\r\n" + content;
            } else {
                std::string notFound = "<html><body><h1>404 Not Found</h1></body></html>";
                response = "HTTP/1.1 404 Not Found\r\n"
                           "Content-Type: text/html\r\n"
                           "Content-Length: " + std::to_string(notFound.size()) + "\r\n"
                           "Connection: close\r\n\r\n" + notFound;
            }

            send(clientSocket, response.c_str(), (int)response.size(), 0);
        }

        closesocket(clientSocket);
    }

    closesocket(listenSocket);
    WSACleanup();
    return 0;
}
