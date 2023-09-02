import random
def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "Lo con cac"
    
    if p_message == 'Lam co iu duy hongg':
        return 'co Lam iuu duyy nhiuu lammm'
    
    if p_message == 'roll 1-10':
        return str(random.randint(1,10))
    
    if p_message == 'roll 1-100':
        return str(random.randint(1,100))


    