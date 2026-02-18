import os
import requests

def send_lead_email(lead_data):
    """
    Send lead notification email via SMTP2GO HTTP API.
    Uses HTTP API instead of raw SMTP because Vercel blocks outbound SMTP ports.
    """
    api_key = os.getenv('SMTP2GO_API_KEY')
    sender_email = os.getenv('SMTP_SENDER') or 'leads@nycscouts.com'
    recipient_email = os.getenv('LEAD_NOTIFICATION_EMAIL') or 'asmarketingltd@gmail.com'
    
    if not api_key:
        print("SMTP2GO_API_KEY not set, skipping email.")
        return False
    
    # Email subject: [Name] - [CampaignCode]
    campaign_code = lead_data.get('campaign', 'N/A')
    subject = f"{lead_data.get('first_name', '')} {lead_data.get('last_name', '')} - {campaign_code}"
    
    # Email body
    body = f"""
New Lead Submission

Name: {lead_data.get('first_name', '')} {lead_data.get('last_name', '')}
Email: {lead_data.get('email', '')}
Phone: {lead_data.get('phone', '')}
Age: {lead_data.get('age', '')}
Gender: {lead_data.get('gender', '')}
City: {lead_data.get('city', '')}
Zip Code: {lead_data.get('zip_code', '')}
Campaign Code: {lead_data.get('campaign', '')}
Score: {lead_data.get('score', '')}
Category: {lead_data.get('category', '')}
Image URL: {lead_data.get('image_url', '')}

Submitted: {lead_data.get('created_at', '')}
"""
    
    try:
        payload = {
            "api_key": api_key,
            "to": [recipient_email],
            "sender": sender_email,
            "subject": subject,
            "text_body": body
        }
        
        response = requests.post(
            "https://api.smtp2go.com/v3/email/send",
            json=payload,
            timeout=10
        )
        
        result = response.json()
        
        if response.status_code == 200 and result.get("data", {}).get("succeeded", 0) > 0:
            print(f"Email sent successfully to {recipient_email}")
            return True
        else:
            print(f"SMTP2GO API error: {result}")
            return False
        
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
        return False
