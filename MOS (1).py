#https://usarmybasic.com/army-jobs/army-mos-list
import sys
import time
import os
def printz(text, delay=0.05):

    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

loopA = 0
loopB = 0
loopC = 0
while loopA == 0:
    os.system("clear")
    printz('Hello, Welcome to the U.S Army MOS List')
    printz("\n\nWhat Category Would you like to Look at first?\nAviation:16 MOS (AVI)\nAir Defense Artillery:4 MOS (ADA)\nOrdnance Corps:47 MOS (OC)\nArmor:4 MOS (ARM)\nTransportation Corps:8 MOS (TC)\nChemical Corps:2 MOS (CC)\nCivil Affairs:2 MOS (CA)\nMilitary Police Corps:4 MOS (MPC)\nFunctional Area:4 MOS (FLA)\nSpecial Forces:8 MOS (SF)\n\n Or go back to Main Menu (MM)")
    categorySelection = input('(Example "AVI"):')
    while loopB == 0:
        if categorySelection == "AVI" or categorySelection == "Avi" or categorySelection == "avi":
            os.system("clear")
            printz("Select the Aviation MOS Branch Job\n15R\n15X\n15Y\n15Q\n15K\n15F\n15Z\n15H\n15B\n15D\n15G\n15O\n15P\n15N\n15U\n15J\n15S\n15T\n15M\n\nOr Back to MOS List (MOS)")
            mosSelect = input('Example "15R" :')
            if mosSelect == "15R" or mosSelect == "15r":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15R\nJob Title: AH-64 Attack Helicopter Repairer\nMOS Branch: Aviation\nShort Description: Supervises and performs maintenance on AH-64 attack helicopters, excluding repair of systems components.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "15X" or mosSelect == "15x":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15X\nJob Title: AH-64A Armament and Electrical System Repairer\nMOS Branch: Aviation\nShort Description: Performs aviation unit (AVUM), intermediate (AVIM), and depot maintenance on the AH-64 electrical and instrument systems and the electrical, electronic, mechanical, and pneudraulics systems associated with AH-64 armament/missile and fire control systems.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif mosSelect == "15Y" or mosSelect == "15y":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15Y\nJob Title: AH-64D Armament/Electrical/Avionics Repairer\nMOS Branch: Aviation\nShort Description: Supervises, inspects, and performs aviation unit, intermediate, and depot maintenance on the AH-64D armament, electrical, and avionic systems, to include the electrical, electronic, mechanical, and pneudraulics systems associated with AH-64D armament/missile fire control systems.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif mosSelect == "15Q" or mosSelect == "15q":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15Q\nJob Title: Air Traffic Control Operator\nMOS Branch: Aviation\nShort Description: Supervises and provides ATC services, to include flight following using visual flight rules (VFR), instrument flight rules (IFR), and special visual flight rules (SVFR), at ATC facilities.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif mosSelect == "15K" or mosSelect == "15k":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15K\nJob Title: Aircraft Components Repair Supervisor\nMOS Branch: Aviation\nShort Description: Supervises aviation unit (AVUM), intermediate (AVIM), and depot maintenance on aircraft components, aviation communications and other electronic/electrical systems associated with Army aircraft. The individual must be knowledgeable of the duties performed by personnel in Army MOS 15B, 15D, 15F, 15G, 15H, and 15N.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif mosSelect == "15F" or mosSelect == "15f":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15F\nJob Title: Aircraft Electrician\nMOS Branch: Aviation\nShort Description: Supervise, inspect, and perform aviation unit (AVUM), intermediate (AVIM), and depot electrical maintenance on aircraft electrical systems.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif mosSelect == "15Z" or mosSelect == "15z":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15Z\nJob Title: Aircraft Maintenance Senior Sergeant\nMOS Branch: Aviation\nShort Description: Supervises aviation unit maintenance (AVUM), intermediate (AVIM), and depot maintenance in activities having a mix of aircraft maintenance and/or component repair Army MOS.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif mosSelect == "15H" or mosSelect == "15h":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15H\nJob Title: Aircraft Pneudraulics Repairer\nMOS Branch: Aviation\nShort Description: Supervise, inspect, and perform aviation unit (AVUM), intermediate (AVIM), and depot maintenance on aircraft pneudraulics systems.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif mosSelect == "15B" or mosSelect == "15b":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15B\nJob Title: Aircraft Powerplant Repairer\nMOS Branch: Aviation\nShort Description: Supervises, inspect, and perform aviation unit (AVUM), intermediate (AVIM), and depot maintenance on aircraft turbine engines and components.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif mosSelect == "15D" or mosSelect == "15d":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15D\nJob Title: Aircraft Powertrain Repairer\nMOS Branch: Aviation\nShort Description: Supervises, inspects, and performs aviation unit (AVUM), intermediate (AVIM), and depot maintenance on aircraft powertrain systems.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif mosSelect == "15G" or mosSelect == "15g":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15G\nJob Title: Aircraft Structural Repairer\nMOS Branch: Aviation\nShort Description: Supervise and perform aviation unit (AVUM), intermediate (AVIM,) and depot maintenance on aircraft structures.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif mosSelect == "15O" or mosSelect == "15o":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15O\nJob Title: Aviation Officer\nMOS Branch: Aviation\nShort Description: An Officer within the Aviation Branch is first an expert aviator, but is also responsible for the coordination of Aviation operations from maintenance to control tower operations to tactical field missions. All Aviation Officers lead Soldiers and Aviation units and work with the following Army helicopters; OH-58 Kiowa, UH-60 Black Hawk, CH-47 Chinook, and AH-64 Apache.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif mosSelect == "15P" or mosSelect == "15p":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15P\nJob Title: Aviation Operations Specialist\nMOS Branch: Aviation\nShort Description: Schedules and dispatches tactical aircraft missions and performs associated operational administrative duties.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif mosSelect == "15U" or mosSelect == "15u":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15U\nJob Title: Medium Helicopter Repairer\nMOS Branch: Aviation\nShort Description: Supervises and performs maintenance on medium helicopters, excluding repair of systems components.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif mosSelect == "15T" or mosSelect == "15t":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15T\nJob Title: UH-60 Helicopter Repairer\nMOS Branch: Aviation\nShort Description: Supervises and performs maintenance on UH-60 helicopters, excluding repair of systems components.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
            elif mosSelect == "15M" or mosSelect == "15m":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 15M\nJob Title: Utility Helicopter Repairer\nMOS Branch: Aviation\nShort Description: Supervises and performs maintenance on UH-1 helicopters, excluding repair of systems components.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loop3 += 1
        elif categorySelection == "ADA" or categorySelection == "Ada" or categorySelection == "ada":
            os.system("clear")
            printz("Select the Air Defense Artillery MOS Branch Job\n14O\n14Z\n14S\n14R\n14J\n14E\n\nOr Back to MOS List (MOS)")
            mosSelect = input('Example "14O" :')
            if mosSelect == "14O" or mosSelect == "14o":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 14O\nJob Title: Air Defense Artillery Officer\nMOS Branch: Air Defense Artillery\nShort Description: The role of an Air Defense Artillery Officer is to be a leader in operations specific to the Air Defense Artillery Branch and to be an expert in the tactics, techniques and procedures for the employment of air defense systems. You will lead teams in protecting U.S. forces from aerial attack, missile attack and enemy surveillance.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "14Z" or mosSelect == "14z":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 14Z\nJob Title: Air Defense Artillery Senior Sergeant\nMOS Branch: Air Defense Artillery\nShort Description: Supervises, plans, coordinates, and directs the emplacement, operation, unit level maintenance and management of air defense artillery weapon systems in support of ADA units at all levels.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "14S" or mosSelect == "14s":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 14S\nJob Title: AVENGER Crewmember\nMOS Branch: Air Defense Artillery\nShort Description: Supervises, operates or serves as a member of a lightweight, highly mobile, Air Defense weapons system.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "14J" or mosSelect == "14j":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 14J\nJob Title: Early Warning System Operator\nMOS Branch: Air Defense Artillery\nShort Description: Supervises or serves as a member of a manual early warning network section, team, or platoon in operations and intelligence functions.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "14E" or mosSelect == "14e":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 14E\nJob Title: PATRIOT Fire Control Enhanced Operator and Maintainer\nMOS Branch: Air Defense Artillery\nShort Description: Supervise or serve in an air defense unit or as a member of an air defense activity engaged in operations or intelligence functions of liaison units.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
        elif categorySelection == "OC" or categorySelection == "Oc" or categorySelection == "oc":
            os.system("clear")
            printz("Select the Ordnance Corps MOS Branch Job\n94D\n91E\n89B\n890A\n45K\n63D\n39B\n915A\n27T\n94L\n94R\n27G\n91L\n94W\n89D\n45G\n63G\n63S\n94Y\n94A\n27E\n63B\n63A\n63M\n44E\n63Z\n44B\n27M\n91O\n94S\n52D\n63J\n94M\n94E\n45D\n94Z\n45B\n42S\n52X\n94J\n94H\n21Y\n63Y\n63H\n52F\n52C\n63W\n94N\n\nOr Back to MOS List (MOS)")
            mosSelect = input('Example "94D" :')
            if mosSelect == "94D" or mosSelect == "94d":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 94D\nJob Title: Air Traffic Control Equipment Repairer\nMOS Branch: Ordnance Corps\nShort Description: Performs unit through intermediate direct support maintenance and installation of ATC communications, navigation aids (NAVAIDS), and landing systems.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "91E" or mosSelect == "91e":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 91E\nJob Title: Allied Trades Specialist (Machinist)\nMOS Branch: Ordnance Corps\nShort Description: The machinist supervises and performs the fabrication, repair, and modifications of metallic and nonmetallic parts and supervises metalworking shop activities.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "89B" or mosSelect == "89b":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 89B\nJob Title: Ammunition Specialist\nMOS Branch: Ordnance Corps\nShort Description: Receives, stores, and issues conventional ammunition, guided missiles, large rockets, and other ammunition related items; performs maintenance (unit, direct support and general support) modification, destruction, and demilitarization on ammunition and explosive components; and operates computer hardware and software/utilities manual records to perform stock control and accounting procedures.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "890A" or mosSelect == "890a":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 890A\nJob Title: Ammunition Technician\nMOS Branch: Ordnance Corps\nShort Description: Ammunition Technician is a warrant officer position which is responsible for receipt, storage, issue, and demilitarization of conventional ammunition and all its components. This position may also be responsible for investigation ammunition accidents and malfunctions, as well as preparing contingency plans for ammunition storage and security.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "45K" or mosSelect == "45k":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 45K\nJob Title: Armament Repairer\nMOS Branch: Ordnance Corps\nShort Description: Supervises and performs direct/general support (DS/GS) and depot level maintenance/repairs on the mechanisms/systems of tank turrets/weapons, fighting vehicles, towed/self-propelled artillery, small arms, and other infantry weapons.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "63D" or mosSelect == "63d":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 63D\nJob Title: Artillery Mechanic\nMOS Branch: Ordnance Corps\nShort Description: Supervises and performs unit maintenance and recovery of all self-propelled field artillery cannon weapon systems, including the automotive, turret, fire control, and chemical protection subsystems thereof.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "39B" or mosSelect == "39b":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 39B\nJob Title: Automatic Test Equipment Operator and Maintainer\nMOS Branch: Ordnance Corps\nShort Description: Operates, maintains, and supervises unit and direct and general support (DS/GS) level maintenance on Automatic Test Equipment (ATE) consisting of electronic equipment test and repair facilities.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "915A" or mosSelect == "915a":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 915A\nJob Title: Automotive Maintenance Warrant Officer\nMOS Branch: Ordnance Corps\nShort Description: Automotive Maintenance is a warrant officer position which plans and performs field maintenance on wheeled and light tracked vehicles, as well as self-propelled artillery systems, ground support, and other powered equipment. As well as fixing malfunctioning equipment, they are also responsible for shop safety, inventory, writing and maintaining Standard Operating Procedures (SOPs), scheduling routine maintenance, and managing the dispatch of available vehicles.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "27T" or mosSelect == "27t":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 27T\nJob Title: AVENGER System Repairer\nMOS Branch: Ordnance Corps\nShort Description: Supervises, performs, and inspects unit level, direct support, and general support maintenance on AVENGER system and associated components (less carrier and communications).")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "94L" or mosSelect == "94l":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 94L\nJob Title: Avionic Communications Equipment Repairer\nMOS Branch: Ordnance Corps\nShort Description: Performs intermediate and depot maintenance on aircraft communications equipment.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "94R" or mosSelect == "94r":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 94R\nJob Title: Avionic Radar Repairer\nMOS Branch: Ordnance Corps\nShort Description: Performs intermediate (AVIM) and depot maintenance on avionic equipment which operates using radar principles..")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "27G" or mosSelect == "27g":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 27G\nJob Title: CHAPARRAL and REDEYE Repairer\nMOS Branch: Ordnance Corps\nShort Description: Supervises or performs direct and general support (DS/GS) level maintenance on the CHAPARRAL and REDEYE missile systems and associated equipment and trainers.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "91L" or mosSelect == "91l":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 91L\nJob Title: Construction Equipment Repairer\nMOS Branch: Ordnance Corps\nShort Description: Supervises and performs unit, direct support and general support (DS/GS) maintenance on construction equipment which includes that used for earth-moving, grading, and compaction; lifting and loading; quarrying and rock crushing; asphalt and concrete mixing and surfacing; water pumping; air compression and pneumatic tools; and powered bridging.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "94W" or mosSelect == "94w":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 94W\nJob Title: Electronic Maintenance Chief\nMOS Branch: Ordnance Corps\nShort Description: Supervises, monitors, and directs the electronics maintenance mission of the US Army, and oversees and performs direct and general support (DS/GS) level maintenance of all Army standard electronics equipment, systems, and associated devices, to include communications security (COMSEC) and controlled cryptographic items (CCI) devices.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "89D" or mosSelect == "89d":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 89D\nJob Title: Explosive Ordnance Disposal Specialist\nMOS Branch: Ordnance Corps\nShort Description: Locates, identifies, renders safe, and disposes of foreign and domestic conventional, chemical, or nuclear ordnance and improvised explosive devices (IED); supports VIP missions for the US Secret Service, State Department, and other Federal agencies.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "45G" or mosSelect == "45g":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 45G\nJob Title: Fire Control System Repairer\nMOS Branch: Ordnance Corps\nShort Description: Supervises and performs direct and general support (DS/GS) maintenance on combat vehicle, infantry and artillery fire control systems and equipment, and related test equipment.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "63G" or mosSelect == "63g":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 63G\nJob Title: Fuel and Electrical Systems Repairer\nMOS Branch: Ordnance Corps\nShort Description: Performs direct support and general support (DS/GS) maintenance on fuel and electrical systems of wheel and track vehicles, brake system components, and on internal combustion engines associated with power generation equipment or material handling equipment.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "63S" or mosSelect == "63s":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 63S\nJob Title: Heavy-Wheel Vehicle Mechanic\nMOS Branch: Ordnance Corps\nShort Description: Performs unit maintenance on heavy-wheel vehicles (prime movers designated as more than 5 tons and their associated trailers) and material handling equipment (MHE).")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "94Y" or mosSelect == "94y":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 94Y\nJob Title: Integrated Family of Test Equipment Operator and Maintainer\nMOS Branch: Ordnance Corps\nShort Description: Operates, performs, and supervises unit, direct support, and general support (DS/GS) level maintenance on the Base Shop Test Facility (BSTF), AN/TSM–191. Performs DS/ GS level electronic maintenance, adjustments, tests, fault isolation, and repairs of supported system line replaceable units (LRU), shop replaceable units (SRU), and test program sets (TPS). Operates and performs preventive maintenance checks and services (PMCS) on assigned vehicles and power generators.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "94A" or mosSelect == "94A":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 94A\nJob Title: Land Combat Electrician\nMOS Branch: Ordnance Corps\nShort Description: Supervises, operates, and performs unit and direct support and general support (DS/GS) level maintenance on Land Combat Support Systems.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "27E" or mosSelect == "27e":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 27E\nJob Title: Land Combat Electronic Missile System Repairer\nMOS Branch: Ordnance Corps\nShort Description: Supervises or performs direct and general support (DS/GS) level maintenance on the TOW and DRAGON missile systems and the Bradley Fighting Vehicle System (BFVS).")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "63B" or mosSelect == "63b":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 63B\nJob Title: Light-Wheel Vehicle Mechanic\nMOS Branch: Ordnance Corps\nShort Description: Supervises and performs unit maintenance and recovery operations on gasoline and diesel fueled light-wheel vehicles (prime movers designated as 5 ton or less and their associated trailers) and associated items. Supervises unit maintenance and recovery operations on track and heavy-wheel vehicles, and on material handling equipment (MHE).")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "63A" or mosSelect == "63a":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 63A\nJob Title: M1 ABRAMS Systems Maintainer\nMOS Branch: Ordnance Corps\nShort Description: 	Supervises and performs unit maintenance and select on-board direct support tasks i.e., major assembly replacement on M1 tanks to include the turret and fire control.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "63M" or mosSelect == "63m":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 63M\nJob Title: M2/3 Bradley Fighting Vehicle System Maintainer\nMOS Branch: Ordnance Corps\nShort Description: Supervises and performs unit maintenance and select on-board direct support task i.e., major assembly and LRU replacement on the M2/M3 A1/A2 series Bradley fighting vehicle, M6 Linebacker, and M7 Bradley Fighting Infantry Support Team (hull and turret).")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "44E" or mosSelect == "44e":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 44E\nJob Title: Machinist\nMOS Branch: Ordnance Corps\nShort Description: Supervises and performs the fabrication, repair, and modifications of metallic and nonmetallic parts and supervises metalworking shop activities.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "63Z" or mosSelect == "63z":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 63Z\nJob Title: Mechanical Maintenance Supervisor\nMOS Branch: Ordnance Corps\nShort Description: Supervises, plans, coordinates, and directs the unit, direct support and general support (DS/GS) maintenance of all mechanical equipment.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "44B" or mosSelect == "44b":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 44B\nJob Title: Metal Worker\nMOS Branch: Ordnance Corps\nShort Description: Supervises, inspects, installs, modifies, and performs maintenance on metal body components, radiators, fuel tanks, hulls, and accessories of Army watercraft and amphibians.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "91O" or mosSelect == "91o":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 91O\nJob Title: Ordnance Officer\nMOS Branch: Ordnance Corps\nShort Description: Ordnance Officers are responsible for ensuring that all weapons systems, vehicles, and equipment are ready and available--and in perfect working order--at all times. An Ordnance Officer will also manage the developing, testing, fielding, handling, storage and disposal of munitions.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "52D" or mosSelect == "52d":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 52D\nJob Title: Power-Generation Equipment Repairer\nMOS Branch: Ordnance Corps\nShort Description: Supervises and performs unit, direct support, and general support (DS/GS) maintenance functions, including overhaul, but not rebuild of power generation equipment, internal combustion engines, and associated equipment up through 200KW (except for turbine engine driven generators).")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "63J" or mosSelect == "63j":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 63J\nJob Title: Quartermaster and Chemical Equipment Repairer\nMOS Branch: Ordnance Corps\nShort Description: Supervises or performs unit and direct support and general support (DS/GS) maintenance on chemical equipment, quartermaster machinery, forced air-heaters, and special purpose equipment.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "94M" or mosSelect == "94m":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 94M\nJob Title: Radar Repairer\nMOS Branch: Ordnance Corps\nShort Description: 	Performs or supervises unit, direct, and general support (DS/GS) level maintenance on Ground Based Sensor (GBS) and FIREFINDER radar electronic assemblies and associated equipment.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "94E" or mosSelect == "94e":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 94E\nJob Title: Radio and Communications Security Repairer\nMOS Branch: Ordnance Corps\nShort Description: Performs or supervises direct and general support (DS/GS) level maintenance of radio receivers, transmitters, COM-SEC equipment, controlled cryptographic items (CCI), and other associated equipment.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "45D" or mosSelect == "45d":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 45D\nJob Title: Self-propelled Field Artillery Turret Mechanic\nMOS Branch: Ordnance Corps\nShort Description: Performs unit maintenance of carriage-mounted armament, associated fire control, and related systems on all self-propelled field artillery weapon systems.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "94Z" or mosSelect == "94z":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 94Z\nJob Title: Senior Electronic Maintenance Chief\nMOS Branch: Ordnance Corps\nShort Description: Plans and directs electronic maintenance operations at all levels of command and echelons of the US Army.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "45B" or mosSelect == "45b":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 45B\nJob Title: Small Arms/Artillery Repairer\nMOS Branch: Ordnance Corps\nShort Description: Performs direct support and general support (DS/GS) maintenance and repairs on small arms, other infantry weapons, and towed artillery.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "94F" or mosSelect == "94f":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 94F\nJob Title: Special Electronic Devices Repairer\nMOS Branch: Ordnance Corps\nShort Description: Performs or supervises direct and general support (DS/GS) level maintenance and repair on special electronic devices, including: night vision equipment, mine detectors, scattering systems, electronic distance and azimuth orienting devices, battlefield illumination devices, electronic azimuth determining devices, and nuclear, biological, and chemical (NBC) warning and measuring devices.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "52X" or mosSelect == "52x":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 52X\nJob Title: Special Purpose Equipment Repairer\nMOS Branch: Ordnance Corps\nShort Description: Supervises the performance of unit, direct support and general support (DS/GS) special purpose equipment maintenance activities. Performs maintenance management activities, including production and quality control.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "94J" or mosSelect == "94j":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 94J\nJob Title: Telecommunication Terminal Device Repairer\nMOS Branch: Ordnance Corps\nShort Description: Performs or supervises direct and general support (DS/GS) level maintenance of microcomputers and electro-mechanical telecommunications terminal equipment, facsimile machines, Field Artillery (FA) digital devices, and other associated equipment and devices.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "94H" or mosSelect == "94h":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 94H\nJob Title: Test, Measurement, and Diagnostic Equipment Support Specialist\nMOS Branch: Ordnance Corps\nShort Description: Performs and supervises duties involving the calibration and repair of general purpose TMDE, selected special purpose TMDE, calibration standards, and accessories. Operates TMDE and calibration standards. Operates and performs preventive maintenance and checks and services (PMCS) on assigned vehicles. Installs, operates, and performs PMCS on power generators.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "63H" or mosSelect == "63h":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 63H\nJob Title: Track Vehicle Repairer\nMOS Branch: Ordnance Corps\nShort Description: Supervises and performs direct support and general support (DS/GS) maintenance on track vehicles; supervises maintenance on wheeled vehicles, material handling equipment (MHE), and chemical quartermaster equipment (less office machines); and supervises related activities including fuel and electrical system repair and maintenance.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "52F" or mosSelect == "52f":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 52F\nJob Title: Turbine Engine Driven Generator Repairer\nMOS Branch: Ordnance Corps\nShort Description: Performs and supervises unit, direct support, and general support (DS/GS) maintenance functions, including overhaul (but not rebuild) of turbine engine driven tactical generator sets, turbine engine prime mover of tactical generator set and associated equipment.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "52C" or mosSelect == "52c":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 52C\nJob Title: Utilities Equipment Repairer\nMOS Branch: Ordnance Corps\nShort Description: Supervises and performs unit, direct support, and general support (DS/GS) maintenance to include utilities equipment and special purpose support systems.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "63W" or mosSelect == "63w":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 63W\nJob Title: Wheel Vehicle Repairer\nMOS Branch: Ordnance Corps\nShort Description: Performs direct support and general support (DS/GS) maintenance on wheel vehicles, material handling equipment (MHE) (less propulsion motor on electrical MHE), trailers, and associated items.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "94N" or mosSelect == "94n":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 94N\nJob Title: Wire Systems Equipment Repairer\nMOS Branch: Ordnance Corps\nShort Description: Performs or supervises direct and general support (DS/GS) level maintenance on manual and semiautomatic unit level switchboards, telephones, and associated wire instruments and equipment.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
        elif categorySelection == "CC" or categorySelection == "Cc" or categorySelection == "cc":
            os.system("clear")
            printz("Select the Chemical Corps MOS Branch Job\n74D\n74O\n\nOr Back to MOS List (MOS)")
            mosSelect = input('Example "74D" :')
            if mosSelect == "74D" or mosSelect == "74d":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 74D\nJob Title: Chemical Operations Specialist\nMOS Branch: Chemical Corps\nShort Description: Operates, performs operator maintenance, or supervises the use of NBC detection and decontamination equipment, smoke generators, and assists in the establishment, administration, training, and application of NBC defense measures. The NBC NCO provides training, advice, and supervision regarding the proper use and maintenance procedures for chemical equipment and chemical operations in company and higher level organizations.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "74O" or mosSelect == "74o":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 74O\nJob Title: Chemical, Biological, Radiological and Nuclear (CBRN) Officer\nMOS Branch: Chemical Corps\nShort Description: CBRN Officers command or serve as a Platoon Leader of a Chemical unit while employing the state-of-the-art CBRN defense systems. In a command and staff role the CBRN Officer, plans, coordinates, and directs CBRN operations and training within a command or activity to include CBRN vulnerability assessment; multi-spectral obscuration; sensitive site exploitation and assessment; CBRN reconnaissance; CBRN decontamination; CBRN force protection; and combating WMD, which includes nonproliferation, counter proliferation, and consequence management.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
        elif categorySelection == "CA" or categorySelection == "Ca" or categorySelection == "ca":
            os.system("clear")
            printz("Select the Civil Affairs MOS Branch Job\n38O\n38B\n\nOr Back to MOS List (MOS)")
            mosSelect = input('Example "38O" :')
            if mosSelect == "38O" or mosSelect == "38o":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 38O\nJob Title: Civil Affairs Officer\nMOS Branch: Civil Affairs\nShort Description: Civil Affairs Officers are experts in acting as a liaison between the Army and civilian authorities and populations. Civil Affairs Officers many times must facilitate relationships between U.S. military forces and the people of the nation(s) in which those forces are operating.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "38B" or mosSelect == "38b":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 38B\nJob Title: Civil Affairs Specialist\nMOS Branch: Civil Affairs\nShort Description: Supervises, researches, coordinates, conducts, and participates in analysis, planning, and production of Civil Affairs related documents and actions encompassing both strategic and tactical Civil Affairs operations for Army, joint, and combined military commands.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
        elif categorySelection == "AMR" or categorySelection == "Amr" or categorySelection == "amr":
            os.system("clear")
            printz("Select the Armor MOS Branch Job\n19O\n19Z\n19D\n19K\n\nOr Back to MOS List (MOS)")
            mosSelect = input('Example "19O" :')
            if mosSelect == "19O" or mosSelect == "19o":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 19O\nJob Title: Armor Officer\nMOS Branch: Armor\nShort Description: The role of an Armor Officer is to be a leader in operations specific to the Armor Branch and to lead others in many areas of combat operations. As an Armor Officer, you may either work with tank units that utilize the M1A1 and M1A2 Abrams Tanks, or cavalry units responsible for forward reconnaissance operations.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "19Z" or mosSelect == "19z":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 19Z\nJob Title: Armor Senior Sergeant\nMOS Branch: Armor\nShort Description: Serve as principal NCO in armor company, cavalry troop, or operations and intelligence staff sections in armor battalion, cavalry squadron, or higher level organizations.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "19D" or mosSelect == "19d":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 19D\nJob Title: Cavalry Scout\nMOS Branch: Armor\nShort Description: Leads, serves, or assists as a member of scout crew, squad, section, or platoon in reconnaissance, security, and other combat operations.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "19K" or mosSelect == "19k":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 19K\nJob Title: M1 Armor Crewman\nMOS Branch: Armor\nShort Description: Leads, supervises, or serves as a member of M1 armor unit in offensive and defensive combat operations. In addition, serves or assists on staffs at battalion or higher level.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
        elif categorySelection == "MPC" or categorySelection == "Mpc" or categorySelection == "mpc":
            os.system("clear")
            printz("Select the Military Police Corps MOS Branch Job\n31E\n31D\n31B\n31O\n\nOr Back to MOS List (MOS)")
            mosSelect = input('Example "31E" :')
            if mosSelect == "31E" or mosSelect == "31e":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 31E\nJob Title: Corrections Specialist\nMOS Branch: Military Police Corps\nShort Description: Controls, supervises, and counsels military prisoners and manages confinement operations and correctional treatment programs.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "31D" or mosSelect == "31d":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 31D\nJob Title: Criminal Investigation Special Agent\nMOS Branch: Military Police Corps\nShort Description: Supervises or conducts investigations of incidents and offenses or allegations of criminality affecting DA or DOD personnel, property, facilities, or activities.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "31B" or mosSelect == "31b":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 31B\nJob Title: Military Police\nMOS Branch: Military Police Corps\nShort Description: Supervise or provide support to the battlefield by conducting battlefield circulation control, area security, prisoner of war operations, civilian internee operations, law and order operations on the battlefield, and support to the peacetime Army community through security of critical Army resources, crime prevention programs, and preservation of law and order.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "31O" or mosSelect == "31o":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 31O\nJob Title: Military Police Officer\nMOS Branch: Military Police Corps\nShort Description: As a Military Police Officer you will be charged with leading soldiers in the execution of offensive operations, defensive operations, stability operations, and civil support operations.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
        elif categorySelection == "FLA" or categorySelection == "Fla" or categorySelection == "fla":
            os.system("clear")
            printz("Select the Functional Area MOS Branch Job\n30AO\n90AO\n57AO\n53AO\n\nOr Back to MOS List (MOS)")
            mosSelect = input('Example "30AO" :')
            if mosSelect == "30AO" or mosSelect == "30Ao" or mosSelect == "30ao":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 30AO\nJob Title: Information Operations Officer\nMOS Branch: Functional Area\nShort Description: The Information Operations Officer is responsible for coordinating, planning and integrating both offensive and defensive Information Operations to gain information superiority in support of the commander's operational concept. Information Operations is integral to every phase of Army and joint planning and operations by linking operational security, psychological operations, deception, electronic warfare, and physical destruction with civil and public affairs capabilities.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "90AO" or mosSelect == "90Ao" or mosSelect == "90ao":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 90AO\nJob Title: Logistics Officer\nMOS Branch: Functional Area\nShort Description: A Logistics Officer keeps a unit moving. They are responsible for planning, developing, and directing the logistical operations of a unit. This position also requires the officer to have experience in integrating the functions of supply, transportation, maintenance, aviation logistics, and medical service into a cohesive unit.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "57AO" or mosSelect == "57Ao" or mosSelect == "57ao":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 57AO\nJob Title: Simulations Operations Officer\nMOS Branch: Functional Area\nShort Description: Simulations Operations Officers are tasked with planning and employing simulations systems in support of training, and combat rehearsal. They may also be responsible for developing doctrine and equipment for the FA57 operations, developing and operating the simulation technology, and assist with simulation systems development.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "53AO" or mosSelect == "53Ao" or mosSelect == "53ao":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 53AO\nJob Title: Systems Automation Management Officer\nMOS Branch: Functional Area\nShort Description: A Systems Automation Management Officer supervises information processing units as well as the installation and activities of those units. They also advise a commander and his staff on effective automation policy and implementation. In addition, they also formulate procedures for contingency operation during system emergencies, outages, or maintenance downtime.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
        elif categorySelection == "SF" or categorySelection == "Sf" or categorySelection == "sf":
            os.system("clear")
            printz("Select the Special Forces MOS Branch Job\n18F\n18E\n18C\n18D\n18O\n18Z\n180W\n18B\n\nOr Back to MOS List (MOS)")
            mosSelect = input('Example "18F" :')
            if mosSelect == "18F" or mosSelect == "18f" or mosSelect == "18f":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 18F\nJob Title: Special Forces Assistant Operations & Intelligence Sergeant\nMOS Branch: Special Forces\nShort Description: Employs conventional and unconventional warfare tactics and techniques in intelligence collection and processing. Trains and maintains proficiency in all major duties. Provides tactical and technical guidance to the Detachment Commander, indigenous and allied personnel. Plans, organizes, trains, advises, assists and supervises indigenous and allied personnel on collection and processing of intelligence information. Performs intelligence and operational duties when task organized in preparation (isolation) for special missions and during operations.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "18E" or mosSelect == "18e" or mosSelect == "18e":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 18E\nJob Title: Special Forces Communications Sergeant\nMOS Branch: Special Forces\nShort Description: Employs conventional and unconventional warfare tactics and techniques in communications.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "18C" or mosSelect == "18c" or mosSelect == "18c":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 18C\nJob Title: Special Forces Engineer Sergeant\nMOS Branch: Special Forces\nShort Description: Employs conventional and unconventional warfare tactics and techniques in combat engineering and maintains detachment engineer equipment and supplies.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "18D" or mosSelect == "18d" or mosSelect == "18d":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 18D\nJob Title: Special Forces Medical Sergeant\nMOS Branch: Special Forces\nShort Description: Employs conventional and unconventional warfare tactics and techniques in providing medical care and treatment.")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1
            elif mosSelect == "18O" or mosSelect == "18o" or mosSelect == "18o":
                while loopC == 0:
                    os.system("clear")
                    printz("MOS: 18O\nJob Title: Special Forces Officer\nMOS Branch: Special Forces\nShort Description: A Special Forces Officer is responsible for what is typically organized as a 12-man team, known as an Operational Detachment Alpha (ODA).")
                    exit = input("\n\nGo Back to the MOS Menu (Yes/No) :")
                    if exit == "Yes" or exit == "yes" or exit == "yes":
                        loopC += 1