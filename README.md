# Nail & Spa Springs

Currently, I live with other people who come from the same country. Especially they just run a business related to ‘Nail & Spa Rusell’ shop. Every day they are very busy because they need to write down some information in a notebook based on a customer's call to make an appointment. Sometimes they say ‘We are losing the customer when we can’t pick up the phone on time’ so they can’t call back at the moment. After they told me about their problem. Finally, I decided to collect more requirements and build the application to support this business in the future. Nail & Spa Rusell is a booking app that helps people book appointments whenever they want. This way, customers do not have to worry about waiting on the phone or physically visiting the Nail & Spa. At the same time, managers now have a way to manage their appointments effectively.

## Table of contents
* [Features](#features)
* [Technologies](#technologies)
* [Installation](#installation)
* [Endpoint API](#endpoint-api)
* [Screenshot](#screenshot)
* [Support this repo](#support-this-repo)
* [Social Contact](#social-contact)
* [Conact Info](#contact-info)


## Features
- Account
  - User Profile
  - Staff Profile
- Shop Profile
  - Category
  - Service
- Make an Appointment
- Time Slot
- Booking
- Notifications
- Promotions
- Review (Refer to service & shop)
- Settings
- Integrated login by Facebook & Google 


## Technologies
#### Backend (Web)
- Python
- Django
- Rest Framework
- Authtoken
- db.sqlite3, PostgreSQL
#### Mobile (iOS)
- Swift 5.3 (Storyboard)
- Compatible OS version: 16
- Compatible Dark & Light Mode
- CoreData 
- RESTFul API
- Alamofire
- SwiftyJSON
- Calendar
- Kingfisher
- Lottie 
- Crashlytics
- Integrated (Facebook & Google)

## Installation
#### Clone the code
```sh
$ https://github.com/ithemecambo/nail_spa_portal
$ cd Nail & Spa Springs 
```

#### Virtualenv modules installation (Unix based systems)
```sh
$ virtualenv env
$ source env/bin/activate
```

#### Install modules
```sh
$ pip install -r requirements.txt
```

#### Create tables
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

#### Create app superuser
```sh
$ python manage.py createsuperuser
```

#### Start the application (development mode)
```sh
$ python manage.py runserver # default port 8000
```

```sh
$ # Access the web app in the browser: Wifi IP Address (Ex: 198.199.50.100:8000)
```


## EndPoint API
#### Server run on port: 8000
```sh
$ # You can change the server depend on your machine settings
$ # (Ex: 192.0.0.1:8000 or localhost:8000) 
$ # BaseUrl = "http://localhost:8000/api/v1/"
```
#### Authenticate by Users
- Get user profile by profile id [GET]
```sh
$ BaseUrl + profile/21/
```

- Create a new user account [POST]
```sh
$ BaseUrl + create-account/
```

- Create a new profile base on account roles [POST]
```sh
$ BaseUrl + create-profile/
```

- Update an existing profile by profile id [PUT]
```sh
$ BaseUrl + update-profile/25/
```

- Upload Avatar to profile by profile id [POST, PUT]
```sh
$ BaseUrl + update-profile/24/
```

- Looking existing an email before allow to register an account [GET]
```sh
$ BaseUrl + 
```

- Login [POST]
```sh
$ BaseUrl + login/
```

- Forget Password depending on account email by profile id [PUT]
```sh
$ BaseUrl + reset-password/21/
```

- Change Password depending on account email by profile id [PUT]
```sh
$ BaseUrl + change-password/21/
```

#### Shop 

- Get Service of Package that selected by shop owner [GET]
```sh
$ BaseUrl + getServices/
```

- Get Shop profile [GET]
```sh
$ BaseUrl + getNailSpa/
```

- Register Device [POST] & [GET]
```sh
$ BaseUrl + getPlatforms/
```

- Notification [POST] & [GET]
```sh
$ BaseUrl + getNotifications/
```

- Promotion [POST] & [GET]
```sh
$ BaseUrl + getPromotions/
```

#### Mak an Appointment
- Get Time Slot by weekday [GET]
```sh
$ BaseUrl + getAppointmentByWeekDays/Saturday/
```

- Make an Appointment [POST]
```sh
$ BaseUrl + appointment/
```

- Create Booking including service [POST]
```sh
$ BaseUrl + booking/
```

#### Booking
- Get Booking by service [GET]
```sh
$ BaseUrl + myBookings/1/Upcoming/
```

- Cancel Booking [PUT]
```sh
$ BaseUrl + cancel-appointment/23/
```

- Reschedule Booking [PUT]
```sh
$ BaseUrl + reschedule-appointment/22/
```

- Review the service of Booking [POST]
```sh
$ BaseUrl + create-review/
```


# Screenshot
#### Backend (Customize Django Admin Interface)
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/web/backend/1.dashboard.png" width="100%">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/web/backend/2.account.png" width="100%">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/web/backend/3.profile.png" width="100%">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/web/backend/4.appointment.png" width="100%">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/web/backend/5.service.png" width="100%">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/web/backend/6.shop.png" width="100%">

#### Mobile (iOS)
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/mobile/iOS/0.1.login.png" width="170"><img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/mobile/iOS/0.2.create-account.png" width="170"><img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/mobile/iOS/1.1.home.png" width="170"><img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/mobile/iOS/1.2.notification.png" width="170">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/mobile/iOS/2.1.appointment.png" width="170">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/mobile/iOS/2.2.appointment.png" width="170">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/mobile/iOS/2.3.appointment.png" width="170">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/mobile/iOS/3.1.booking.png" width="170">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/mobile/iOS/3.2.reschedule-booking.png" width="170">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/mobile/iOS/3.3.cencel-booking.png" width="170">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/mobile/iOS/3.4.completed-booking.png" width="170">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/mobile/iOS/3.5.review-booking.png" width="170">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/mobile/iOS/4.1.account-settings.png" width="170">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/mobile/iOS/4.2.account-info.png" width="170">
<img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/mobile/iOS/4.3.shop-location.png" width="170">


## Support this repo
* Star this repo <img src="https://github.com/ithemecambo/nail_spa_portal/blob/main/screenshots/give-star.png" width="60">


## Social Contact
* LinkedIn: <a href="https://www.linkedin.com/in/senghortkheang">kheang senghort</a>
* Portfolio: <a href="https://ithemecambo.github.io/portfolio">Senghort Kheang</a>


## Contact Info
* Email: senghort.rupp@gmail.com
