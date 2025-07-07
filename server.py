from typing import Dict, Optional, List
from mcp.server.fastmcp import FastMCP
from HRMS import *
from utils import seed_services
from email_sender import send_email

mcp = FastMCP("Agentic-HR-Assist")

employee_manager = EmployeeManager()
leave_manager = LeaveManager()
ticket_manager = TicketManager()
meeting_manager = MeetingManager()

seed_services(employee_manager, leave_manager, meeting_manager, ticket_manager)

@mcp.tool()
def add_employee(emp_name: str, email: str, manager_id: Optional[str] = None) -> str:
    emp = EmployeeCreate(
        emp_id=employee_manager.get_next_emp_id(),
        name=emp_name,
        manager_id=manager_id,
        email=email,
    )
    employee_manager.add_employee(emp)
    return f"Employee {emp_name} added successfully."

@mcp.tool()
def get_employee_details(name: str) -> Dict[str, str]:
    matches = employee_manager.search_employee_by_name(name)[0]

    if len(matches) == 0:
        raise ValueError(f"No Employees found with name '{name}'.")
    
    return employee_manager.get_employee_details(matches)

@mcp.tool()
def email_sender(receiver_emails: List[str], subject: str, body: str):
    send_email(
        receiver_emails=receiver_emails,
        subject=subject,
        body=body,
    )

    return "Email sent successfully!"

@mcp.tool()
def create_ticket(employee_id: str, item: str, reason: str):
    ticket_req = TicketCreate(
        emp_id=employee_id,
        item=item,
        reason=reason
    )

    ticket_manager.create_ticket(ticket_req)

@mcp.prompt("onboard_new_employee")
def onboard_new_employee(employee_name: str, manager_name: str, employee_email: str):
    return f"""
    Onboard a new employee with the following details:

    Name: {employee_name}

    Email: {employee_email}

    Manager: {manager_name} or 'None' if no manager. 

    The process should:

    Add the employee to the HRMS system with a unique employee ID.

    Assign the manager if provided (skip if 'None').

    Retrieve and confirm the employee details after creation.

    Automatically send a welcome email to the new employee with a subject like ‘Welcome to the Team, {employee_name}!’ and a warm, professional message including their manager’s name, first-day info (reporting at 9:30 AM, business casual, carry govt. ID), and a note of encouragement.
    If manager is 'None', don't include anything about manager in the email.

    Send a notification email to assignment of the new employee to the manager.

    Raise tickets for a new laptop, id card, and other essential items.

    Ensure everything is done in one go.
    """

if __name__ == '__main__':
    mcp.run(transport='stdio')
