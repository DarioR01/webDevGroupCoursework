# list of group members

# Contributors
## Russo Dario
Contribution:
- Redesign using django framework `..bidder/api/login` view 
- Redesign using django framework`..bidder/api/register` view
- Redesign using django framework`..bidder/api/logout` view   
- Upload image Proof Of Concept
- Implement email send handler and crontab
- Implement redesign for login
- Implement registration page
- Implement home page frontend
- Implement Item Page frontend 
- Implement Vue Routing

## Stancheva Yanitsa
Contribution:
- Application design
- First login page iteration
- Implement frontend for user profile page
- Implement frontend for profile update
- Implement frontend for create item

## Iandiorio Virginia
Contribution:
- Application design
- User model desing
- `..bidder/api/login` view with linked utils functions
- `..bidder/api/register` view with linked utils functions
- `..bidder/api/logout` view with linked utils functions
- `..bidder/api/home` view with linked utils functions
- `..bidder/api/home/(?P<filter>\w+)/$` view with linked utils functions
- `..bidder/api/item/<int:item_id>` view with linked utils functions
- `..bidder/api/item/<int:item_id>/<int:question_id>` view with linked utils functions
- redesign - `..bidder/api/profile` view with linked utils functions
- redeisng `..bidder/api/profile/<int:item_id>` view with linked utils functions
- `..bidder/api/profile/<int:item_id>` upload image full implementation
- backend testing

## Svarca Orgesa
Contribution:
- Item model design
- Question model design
- `..bidder/api/profile` view with linked utils functions
- `..bidder/api/profile/<int:item_id` view with linked utils functions
- Openshift Deployment

# URL of deployed application
N/A

# Username and password for the admin page
start your experience from localhost:8000/bidder/api/login
## Admin user:
username: `superuser@gmail.com`
password: `1234`
# Username and passwords of the 5 test users

## Test user 1:
username: `user1@gmail.com`
password: `1234`

## Test user 2:
username: `user2@gmail.com`
password: `1234`

## Test user 3:
username: `user3@gmail.com`
password: `1234`

## Test user 4:
username: `user4@gmail.com`
password: `1234`

## Test user 5:
username: `user5@gmail.com`
password: `1234`

# Local App
You will need 2 terminals

frontend:

```bash
cd auction_frontend
npm install
npm run dev
```

If migration are alredy created backend:

```bash
python manage.py runserver
```

If migrations are not yet performed:

```bash
python manage.py makemigrations welcome
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Frontend pages overview:

## Home Page:
Shows item that are submitted in the profile page (Only shows items that have an in-progress bid)
Filter items by keywords (This uses both name and description of the item)
Link to single item pages by clicking on the item

## Profile Page:
In Profile page you can:
- Update user's information
- Update user's image
- Post a new item

## Single Item Page:
In single item page you can:
- Bid for an item
- Ask question
- Answer questions (Only the owner of the item can answer question, otherwise you will get an alert())

# Backend overview:
- Only jpg image are allowed.
- Price is in Integer