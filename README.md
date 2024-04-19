The platform will offer users the option to view a collective gallery of all pet photos, enabling them to explore and engage with the vibrant pet community. Users can open detailed views of individual photos, express their appreciation by liking them, and share their thoughts through comments.
1.1.Routes
Home Page: http://127.0.0.1:8000/ 
Registration Page: http://127.0.0.1:8000/accounts/register/ 
Login Page: http://127.0.0.1:8000/accounts/login/ 
Profile Details Page: http://127.0.0.1:8000/accounts/profile/<int:pk>/ 
Profile Edit Page: http://127.0.0.1:8000/accounts/profile/<int:pk>/edit/ 
Profile Delete Page: http://127.0.0.1:8000/accounts/profile/<int:pk>/delete/ 
Pet Add Page: http://127.0.0.1:8000/pets/add/ 
Pet Details Page: http://127.0.0.1:8000/pets/<str:username>/pet/<slug:pet_slug>/ 
Pet Edit Page: http://127.0.0.1:8000/pets/<str:username>/pet/<slug:pet_slug>/edit/
Pet Delete Page: http://127.0.0.1:8000/pets/<str:username>/pet/<slug:pet_slug>/delete/ 
Photo Add Page: http://127.0.0.1:8000/photos/add/ 
Photo Details Page: http://127.0.0.1:8000/photos/<int:pk>/ 
Photo Edit Page: http://127.0.0.1:8000/photos/<int:pk>/edit/
