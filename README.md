# IHRD_PMD_Software_Developer_Backend

# Django Task

1. **Home Page Accessibility:** Ensure that the home page of the application is accessible and functioning properly.
![alt text](https://drive.google.com/file/d/1btYMhjLKNKOpSPbQ35u0I2t25cskyBzU/view?usp=sharing)

# Check if email or phone number already exists in registration
 
	 if get_user_model().objects.filter(email=email).exists():
	      return Response({'code': 400, 'message': 'Email already exists'})
      
      
# Authenticate the user in login function 
        user = get_user_model().objects.filter(email=email).first()
        
# Update last login time
            user.last_login = timezone.now()
            user.save()
 
# Generate JWT tokens
  from rest_framework import status
  from rest_framework_jwt.settings import api_settings
            payload = jwt_payload_handler(user)
            access_token = jwt_encode_handler(payload)
            
# login success 

	 HTTP 200 OK
	Allow: POST, OPTIONS
	Content-Type: application/json
	Vary: Accept

	{
	    "code": 200,
	    "message": "success",
	    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImFuc2FoMTIzQGdtYWlsLmNvbSIsImV4cCI6MTcwMDc1NTI2MiwiZW1haWwiOiJhbnNhaDEyM0BnbWFpbC5jb20ifQ.4ZxVjPyBN1RxTD8KfxoONkqJbeIUh83gM2nbojXI-RA",
	    "refresh_token": "refresh_token",
	    "user_id": 2,
	    "name": "ansah",
	    "email": "ansah123@gmail.com",
	    "last_login": "2023-11-23T15:56:02.840596"
	}
