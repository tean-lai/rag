#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

int main() {
  const std::string filename = "data/documents.json";

  std::ifstream file(filename);
  if (!file.is_open()) {
    std::cerr << "Failed to open " << filename << "\n";
    return 1;
  }

  json j;
  try {
    file >> j;
  } catch (const json::parse_error &e) {
    std::cerr << "JSON parse error: " << e.what() << "\n";
    return 1;
  }
}
