# Internal-Network-Management-System-INMS

A comprehensive web application built with Django designed to help institutions (such as companies or schools) efficiently manage their internal networks.

## Features
- Network Device Management: Track and manage all networking devices connected to the network
- Event Registration: Log and monitor network events (such as communication interruptions)
- Reporting: Generate detailed reports on network usage and performance
- User Management: Role-based access control for different user types
- Dashboard: Real-time network status and metrics visualization

## Technology Stack
- Backend: Django
- Database: SQLite (development), PostgreSQL (production)
- Frontend: HTML, CSS, JavaScript
- Authentication: Django's built-in authentication system

## Installation

Prerequisites:
- Python 3.8+
- pip

Steps:
1. Clone the repository:
   git clone https://github.com/alanhasn/Internal-Network-Management-System.git
2. Navigate to the project directory:
   cd Internal-Network-Management-System
3. Create a virtual environment:
   python -m venv venv
4. Activate the virtual environment:
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
5. Install dependencies:
   pip install -r requirements.txt
6. Run migrations:
   python manage.py migrate
7. Create a superuser:
   python manage.py createsuperuser
8. Run the development server:
   python manage.py runserver

## Usage
- Access the application at http://localhost:8000
- Use the admin panel at http://localhost:8000/admin
- Login with the superuser credentials created during installation

## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Contact
For any questions or suggestions, please open an issue or contact:
- Email: whoamialan@gmail.com
- GitHub: https://github.com/alanhasn
