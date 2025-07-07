# 🚀 Agentic-AI-HR-Assistant

A comprehensive Human Resources Management System (HRMS) built with FastMCP that provides automated employee onboarding, management, and administrative tools.

## 🌟 Overview
Agentic HR Assist is an intelligent HR assistant that streamlines common HR processes including employee management, automated email communications, ticket creation for IT resources, and complete employee onboarding workflows.

## 🎯 Features

1. Employee Management: Add, search, and retrieve employee details
2. Automated Email System: Send welcome emails and notifications
3. Ticket Management: Create tickets for IT resources (laptops, ID cards, etc.)
4. Complete Onboarding Workflow: Automated end-to-end employee onboarding process
5. Manager Assignment: Support for hierarchical employee-manager relationships

## 🚀 Installation

1. 📥 Clone the repository.
2. 📦 Install required dependencies:
pip install fastmcp

3. 🔧 Ensure the following modules are available:
  a. HRMS - Core HR management system
  b. utils - Utility functions and seed data
  c. email_sender - Email functionality



## 💻 Usage

### 🏃‍♂️ Running the Server
python main.py
🌐 The server runs on stdio transport and provides MCP (Model Context Protocol) tools for AI agents.

### 🛠️ Available Tools
**add_employee(emp_name, email, manager_id=None)**
Adds a new employee to the HRMS system.

### Parameters:

**emp_name (str)**: Employee's full name
**email (str)**: Employee's email address
**manager_id (str, optional)**: Manager's employee ID

### Returns: Success confirmation message
🔍 **get_employee_details(name)**
Retrieves detailed information about an employee by name.

### Parameters:

**name (str)**: Employee name to search for

### Returns: Dictionary containing employee details
📧  **email_sender(receiver_emails, subject, body)**
Sends emails to specified recipients.

### Parameters:

1. **receiver_emails (List[str])**: List of recipient email addresses
2. **subject (str)**: Email subject line
3. **body (str)**: Email content

### Returns: Success confirmation message
🎫 **create_ticket(employee_id, item, reason)**
Creates a ticket for IT resources or administrative requests.

### Parameters:

**employee_id** (str): Employee ID requesting the item
**item** (str): Item being requested (e.g., "laptop", "ID card")
**reason** (str): Reason for the request

### 🎨 Prompts
🌟 **onboard_new_employee**
Comprehensive employee onboarding workflow that handles:

### Parameters:

1. **employee_name (str)**: New employee's name
2. **manager_name (str)**: Manager's name or 'None' if no manager
3. **employee_email (str)**: New employee's email

### 🔄  Process includes:

1. Adding employee to HRMS with unique ID
2. Manager assignment (if provided)
3. Employee details confirmation
4. Welcome email to new employee
5. Notification email to manager
6. Automatic ticket creation for essential items:

  a. Laptop
  b. ID card
  c. Other necessary equipment



### System Components
🎯 **Core Managers**

**EmployeeManager**: Handles employee data and operations
**LeaveManager**: Manages employee leave requests
**TicketManager**: Processes IT and administrative tickets
**MeetingManager**: Handles meeting scheduling and management

### Initialization
The system uses **seed_services()** to populate initial data for testing and development.

### 📧 Email Templates

#### Welcome Email

1. Subject: "Welcome to the Team, {employee_name}!"
2. Includes manager information, first-day instructions, and encouragement
3. Provides essential information: reporting time (9:30 AM), dress code (business casual), required documents (govt. ID)

**Manager Notification**

Notifies managers of new team member assignments
Includes new employee details and start date

**Error Handling**
The system includes comprehensive error handling:

1. Employee search validation
2. Email delivery confirmation
3. Ticket creation verification

## 📚 Dependencies

FastMCP framework for MCP server implementation
Custom HRMS modules for core functionality
Email service integration

## 🤝 Contributing

Fork the repository
Create a feature branch
Make your changes
Submit a pull request

## 🆘 Support

If you have any questions or need support, please reach out on: GitHub: @krishnasahu29 LinkedIn: www.linkedin.com/in/krishnasahu29 Email: krishna.sahu.work222@gmail.com
