from wtforms import Form, SelectField, validators, IntegerField, DecimalField, SelectMultipleField

class CreateUserForm_regression(Form):
    accommodates = IntegerField('Maximum Number of guests it can accomodate:', [validators.DataRequired()])
    availability_30 = IntegerField('Number of days it is available for booking within the next 30 days:', [validators.DataRequired(), validators.NumberRange(min=0,max=30,message='Invalid')])
    bathrooms = IntegerField('Number of bathrooms available in the accommodation:', [validators.DataRequired()])
    bedrooms = IntegerField('Number of bedrooms available in the accommodation:', [validators.DataRequired()])
    beds = IntegerField('Number of beds available in the accommodation:', [validators.DataRequired()])
    calculated_host_listings_count = IntegerField('Total number of listings the host has across all properties:', [validators.DataRequired()])
    host_listings_count = IntegerField('Total number of listings the host has for the specific:', [validators.DataRequired()])
    cancellation_policy = SelectField('Strictness of cancellation policy:', [validators.DataRequired()], choices=[('','Please Select...'),('Flexible',"Flexible"),('Moderate','Moderate'),('No','No Refunds'),('Strict','Strict'),('Very','Very Strict')], default='')
    guests_included = IntegerField('Number of guests included in the base price:', [validators.DataRequired()])
    maximum_nights = IntegerField('Maximum number of nights that a guest can book:', [validators.DataRequired()])
    number_of_reviews = IntegerField('Total number of reviews it has received:', [validators.DataRequired()])
    review_scores_communication = IntegerField('Rating score for communications (out of 10):', [validators.DataRequired(), validators.NumberRange(min=0,max=10,message='Invalid')])
    review_scores_location = IntegerField('Rating score for location (out of 10):', [validators.DataRequired(), validators.NumberRange(min=0,max=10,message='Invalid')])
    review_scores_value = IntegerField('Rating score for value (out of 10):', [validators.DataRequired(), validators.NumberRange(min=0,max=10,message='Invalid')])
    review_scores_rating = IntegerField('Overall rating score (out of 100):', [validators.DataRequired(), validators.NumberRange(min=0,max=100,message='Invalid')])
    room_type = SelectField('Room Type:', [validators.DataRequired()], choices=[('','Please Select...'),('Entire',"Entire Home/Apartment"),('Private','Private Room'),('Shared','Shared Room')], default='')
    amenities = SelectMultipleField('Select amenities the accomodation has:', choices=[('Cable','Cable TV'),('Carbon',"Carbon Monoxide Detector"),('Doorman','Doorman'),('Elevator','Elevator in Building'),('Family','Family/Kid Friendly'),('Extinguisher','Fire Extinguisher'),('Firstaid','First Aid Kit'),('Tub','Hot Tub'),('Fireplace','Indoor Fireplace'), ('Pets','Pets Allowed'),('Pool','Pool'),('Shampoo','Shampoo'),('Smoke','Smoke Detector'),('Events','Suitable for Events')], default='') 

class mushroom_form(Form):
    flat_cap = SelectField('Is the mushroom cap flat?:', [validators.DataRequired()], choices=[('','Please Select...'),('Yes',"Yes"),('No','No')], default='')
    bruises = SelectField('Bruises?:', [validators.DataRequired()], choices=[('','Please Select...'),('Yes',"Yes"),('No','No')], default='')
    odor = SelectField('Any odor?:', [validators.DataRequired()], choices=[('','Please Select...'),('No',"No"),('Yes','Yes')], default='')
    gillsize = SelectField('Gill Size:', [validators.DataRequired()], choices=[('','Please Select...'),('Broad',"Broad"),('Narrow','Narrow')], default='')
