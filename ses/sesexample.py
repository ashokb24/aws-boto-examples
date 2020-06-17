from typing import List

import boto3
import json


class SESResource:
    def __init__(self, region_name):
        self.region_name = region_name
        self.ses_client = boto3.client('ses', region_name=self.region_name)

    def send_mail_using_template(self, template_name=None, sender_email_address=None, recipient_email_addresses=None):
        template_data = "{\"name\": \"Ashok Bhadrappa\"}"
        response = self.ses_client.send_templated_email(
            Source=sender_email_address,
            Destination={
                'ToAddresses': [
                    recipient_email_addresses
                ]
            },
            Template=template_name,
            TemplateData=json.dumps(template_data)
        )
        return response

    def verify_email_address(self, to_be_verified_email_address=None):
        response = self.ses_client.verify_email_identity(EmailAddress=to_be_verified_email_address)
        print(response)
        return response

    def create_http_email_template(self):
        html_mail_template_file = open("mailtemplates/contactusautoreply.html", 'r', encoding='utf-8')
        body_html = html_mail_template_file.read()
        response = self.ses_client.create_template(
            Template={
                'TemplateName': 'contact_us_reply_http_template',
                'SubjectPart': 'Thank you for contacting us, {{name}}',
                'HtmlPart': body_html
            }
        )

        return response

    def create_text_email_template(self):
        # The email body for recipients with non-HTML email clients.
        text_mail_template_file = open("mailtemplates/contactusautoreply.txt", 'r', encoding='utf-8')
        text_html = text_mail_template_file.read()
        response = self.ses_client.create_template(
            Template={
                'TemplateName': 'contact_us_reply_text_template',
                'SubjectPart': 'Thank you for contacting us, {{name}}',
                'TextPart': text_html
            }
        )
        return response

    def delete_mail_templates(self, template_names=None):
        for template_name in template_names:
            response = self.ses_client.delete_template(TemplateName=template_name)
        return

    def view_mail_template(self, template_name=None):
        response = self.ses_client.get_template(TemplateName=template_name)
        print(response)
        return response

    def verify_domain_names(self,domain_names=None):
        response = []
        for domain_name in domain_names:
            response.append(self.ses_client.verify_domain_identity(Domain=domain_name))
            response.append("\r\n")
        return response


if __name__ == '__main__':
    ses_object = SESResource("ap-south-1")
    # ses_object.verify_email_address(to_be_verified_email_address="ashokb.24@hotmail.com")
    # ses_object.create_http_email_template()
    # ses_object.create_text_email_template()
    # ses_object.delete_mail_templates(template_names=["contact_us_reply_http_template",
    #                                                  "contact_us_reply_text_template"])
    # ses_object.view_mail_template(template_name="contact_us_reply_text_template")
    # domain_names = ['hotmail.com','gmail.com','yahoo.com', 'live.com','rediffmail.com']
    # ses_object.verify_domain_names(domain_names)
    # recipient_email_address = "ashokb08@gmail.com"
    # ses_object.send_mail_using_template(template_name='contact_us_reply_http_template',
    #                                     sender_email_address="ashokb.24@hotmail.com",
    #                                     recipient_email_addresses=recipient_email_address)
