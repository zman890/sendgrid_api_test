Feature: Send email through Web API
Scenario: Send email
Given I visit "http://sendgrid.com/docs/api_workshop.html"
When I login as user "user" with password "password"
And I display the mail form
And I fill in the 'to' field with 'you@example.com' 
And I fill in the 'toname' field with 'Sample Recipient' 
And I fill in the 'x-smtpapi' field with '{"filters" : {"clicktrack" : {"settings" : {"enable" : 1}}}}'
And I fill in the 'from' field with 'you@example.com'
And I fill in the 'fromname' field with 'Sample Sender'
And I fill in the 'subject' field with 'SendGrid test'
And I fill in the 'text' field with 'Hello world!'
And I fill in the 'html' field with '<h3>Welcome valued customer!</h3>'
And I fill in the 'bcc' field with 'you@example.com'
And I fill in the 'date' field with 'Thu, 12 Dec 2013 08:30:52 -0700 (MST)'
And I fill in the 'headers' field with '{ "X-SA-userid": "7682171" }'
And I fill in the 'files' field with 'files[file1.doc]=example.doc'
And submit the form
Then the response should indicate success
