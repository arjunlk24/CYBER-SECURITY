import hashlib

def generate_hashes():
    print("Choose a hash algorithm which you want to practice on: ")
    print("1. MD5")
    print("2. SHA1")
    print("3. NT Hash")
    choice = input("Enter your choice: ")

    if choice == '1':
        algorithm = hashlib.md5
    elif choice == '2':
        algorithm = hashlib.sha1
    elif choice == '3':
        # NT Hash is a variant of MD4, commonly used in Windows authentication systems
        algorithm = lambda x: hashlib.new('md4', x.encode('utf-16le')).digest()
    else:
        print("Invalid choice")
        return

    text = input("Enter the word or sentence to convert into hash: ")
    hashed_text = algorithm(text.encode()).hexdigest()

    output_file = input("Enter the name of the output file: ")
    with open(output_file, 'w') as file:
        file.write(hashed_text)
    print(f"Hash has been saved to {output_file}")

if __name__ == "__main__":                                                                                              
    # print("                                        :~::^.                ^YBG###5:                   ")         
    # print("                                       JB#B##BY:             !#######&!                   ")         
    # print("                                      J&######&J             P###BG##B:                   ")         
    # print("                                     ~####B####7            !####5B##Y                    ")         
    # print("                                     Y####PB###:            5####G###~                    ")         
    # print("                                    .B####B###P            .G#######G                     ")         
    # print("                                    ~#########J            ~########Y                     ")         
    # print("                                    Y#########7            ?&#######!                     ")         
    # print("                                   .B#########^            P########:                     ")         
    # print("                                   ~#########G^::::^^^^^^^~B##G####B!~~~~~~~~~~^^::...... ")         
    # print("               .7Y5PPPPPPPPPPPPPPGGB##########B#################################BBGGP5YJ!:")         
    # print("              .7B&###########################################################BP55Y?7~:    ")         
    # print("              .?G##############################################################BPJ!...    ")         
    # print("               .JG##########&&&&&############################BB############BBBGG5J?~      ")         
    # print("                 .^~~!!!!777??????G5#######G!!!!!!!!!!!!~P##5PB###?^~^^^^^:::...          ")         
    # print("                                 ^G5#######J            :B#B5G####:                       ")         
    # print("                                 J####B####~            J&#55B###P                        ")         
    # print("                                 57B#B####B.           .G##J5B###7                        ")         
    # print("                                ~GJ#PJB###Y            :B#P?Y###B:                        ")         
    # print("                                YYB#Y?B###!            7##JYP###5                         ")         
    # print("             .::::^^^^^^^^^^^^^^P7GBP####B7!!77?7?JJJJJG#BPB####G555555555YYYJJ?7^        ")         
    # print("            .7PBBBB#######GPGB#B####BB###BB#####B#&###&########################&&B~       ")         
    # print("           .~7YGGPPB#######BB###############BBB##########B######BBBBBGGGGGGB#####&Y.      ")         
    # print("        ^7Y5GGB#&&&&#####################&&####################BBBBBBBBBBBBGGGPP5?:       ")         
    # print("        ..::^^~!7??JJJJYYY5555BBBB#P####5J????7!!~~^~B##PGG###5......:......              ")         
    # print("                             !BP##BJ###G.           ?##BGB####~                           ")         
    # print("                             P##B#Y5###J            G########P                            ")         
    # print("                            ~##GG#Y####^           ^########&7                            ")         
    # print("                            ?&#J5#B###P            !########B:                            ")         
    # print("                            5#B?G#####7            7#B##B###Y                             ")         
    # print("                           .B#G!B####P.            ~#PG#G###~                             ")         
    # print("                           .5BG!#B###!             :JG?GP##G.                             ")         
    # print("                             :?.JG##5               .?^PP##?                              ")         
    # print("                                .7BB:                 ..J&B:                              ")         
    # print("                                  ^~                    !YY                               ")         
    # print("                                                          .                               ")     
    print("█████████████████████████████████████████████████████████████████████████████████████████████████████████")
    print("█▌                                                                                                     ▐█")
    print("█▌  █████   █████   █████████    █████████  █████   █████ ███████████    █████████     █████████       ▐█")
    print("█▌ ░░███   ░░███   ███░░░░░███  ███░░░░░███░░███   ░░███ ░░███░░░░░███  ███░░░░░███   ███░░░░░███      ▐█")
    print("█▌  ░███    ░███  ░███    ░███ ░███    ░░░  ░███    ░███  ░███    ░███ ░███    ░███  ███     ░░░       ▐█")
    print("█▌  ░███████████  ░███████████ ░░█████████  ░███████████  ░██████████  ░███████████ ░███               ▐█")
    print("█▌  ░███░░░░░███  ░███░░░░░███  ░░░░░░░░███ ░███░░░░░███  ░███░░░░░░   ░███░░░░░███ ░███               ▐█")
    print("█▌  ░███    ░███  ░███    ░███  ███    ░███ ░███    ░███  ░███         ░███    ░███ ░░███     ███      ▐█")
    print("█▌  █████   █████ █████   █████░░█████████  █████   █████ █████        █████   █████ ░░█████████       ▐█")
    print("█▌ ░░░░░   ░░░░░ ░░░░░   ░░░░░  ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░        ░░░░░   ░░░░░   ░░░░░░░░░        ▐█")
    print("█▌                                                                                                     ▐█")
    print("█████████████████████████████████████████████████████████████████████████████████████████████████████████")
    generate_hashes()
    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                
