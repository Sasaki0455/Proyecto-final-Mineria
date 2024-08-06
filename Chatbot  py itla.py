import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Preguntas y respuestas sobre el ITLA
    response('El ITLA es el Instituto Tecnológico de las Américas, una institución educativa especializada en tecnologías.', 
             ['qué', 'es', 'itla', 'instituto', 'tecnológico', 'américas'], single_response=True)
    
    response('Esta ubicada en Las Américas Highway, Km. 27, La Caleta, Calle 27.', 
             ['Como',  'llegar', 'Donde', 'Esta', 'ubicado', 'itla'], single_response=True)
    
    response('Puedes aplicar visitando nuestra página web y llenando el formulario de inscripción.', 
             ['aplicar', 'requisitos', 'admisión', 'inscripción', 'proceso'], single_response=True)
    
    response('El costo de la incripcion son de 6640 pesos.', 
             ['Cuanto', 'incripcion','monto','cuesta', 'pesos','costo'  ], single_response=True)
    
    response('El ITLA organiza talleres y seminarios en tecnología para estudiantes y profesionales.', 
             ['talleres', 'seminarios', 'tecnología', 'organiza'], single_response=True)
    
    response('Sí, ofrecemos diversas becas y ayudas financieras. Puedes aplicar a ellas a través de nuestra página web.', 
             ['becas', 'ayudas', 'financieras', 'tipos', 'cómo', 'aplicar'], single_response=True)
    
    response('Tenemos horarios diurnos y nocturnos, y algunas clases están disponibles en línea.', 
             ['horarios', 'clases', 'línea', 'modalidad', 'estudio'], single_response=True)
    
    response('Nuestras instalaciones incluyen laboratorios modernos, bibliotecas, y áreas deportivas.', 
             ['instalaciones', 'facilidades', 'infraestructura', 'visitar', 'campus'], single_response=True)
    
    response('Ofrecemos una variedad de actividades extracurriculares, incluyendo clubes estudiantiles y deportes.', 
             ['actividades', 'extracurriculares', 'clubes', 'deportes', 'practicar'], single_response=True)
    
    response('El ITLA tiene convenios con varias universidades internacionales para intercambios académicos.', 
             ['convenios', 'intercambios', 'universidades', 'internacionales'], single_response=True)
    
    response('Puedes contactarnos al número (809) 738-4852 o a través del correo info@itla.edu.do.', 
             ['contactar', 'número', 'teléfono', 'correo', 'electrónico', 'contacto'], single_response=True)

    best_match = max(highest_prob, key=highest_prob.get)
    # print(highest_prob)

    return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['¿Puedes decirlo de nuevo?', 'No estoy seguro de lo que quieres', 'Búscalo en Google a ver qué tal'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))
