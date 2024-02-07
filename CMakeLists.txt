cmake_minimum_required(VERSION 3.5)
project(articubot_one)

# Busca paquetes requeridos
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

# Indica que no se debe compilar el script Python
#ament_python_install_package(${PROJECT_NAME})

# Instala el script Python en el directorio de instalación
install(PROGRAMS
  robot_square.py
  DESTINATION lib/${PROJECT_NAME}
)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Configuraciones específicas del compilador (opcional)
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

# Instala directorios adicionales (config, description, launch, worlds, src)
install(
  DIRECTORY config description launch worlds 
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
