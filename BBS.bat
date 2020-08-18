@echo off   
title Black Box Security 
color 0b                                                                                              
@echo		                                                            `/o/`                                 
@echo		                                                           -dmmdds/-.                               
@echo		                                                    .oddhsymNNNmdddddh+`                            
@echo		                                            `y:`  -smNNNNNNNNmmNdddddddy-                           
@echo		                                            /NmdhdmNdsssdmho:..+hdddddddds-                       
@echo		                                            -mNNNNd+omNdysydmmdo:ohyso++sdd/                        
@echo		                                            .ohdho+dNNMMMMMMNNMNmyyddddy./dd/                       
@echo		                                            yd:+s+:://mMMMMh/::+hNNNNNNm-:ddd`                      
@echo		                                            :/oNoohmNNMMMMMMNmds-sNNNNy-odddd`                      
@echo		                                            -NMM-  /MMsyMMM+`  -mNNNNNyo+o+d+                       
@echo		                                            yMMMs-:dm+oMMMM+`  .mNNNNNho++o/`                       
@echo		           `/shh+                           NMMMMMMh.sMMMMMNdhhNMNNNNNysyo:                         
@echo		          `dMMMMh                           MMMMMMMy`oNMMMMMMMMMNNNNNNssmd`                         
@echo		          +MMMMM/                           mMMmNMMMdyNMMMMm+dNMNNNNNNNNNN+                         
@echo		          +MMMMN`                           sM+.:+hmmmmdyo/:  -mNNNNNNNNNNy                         
@echo		          `mMMNN:                           .Ns..`  ``     `:o.mNNNNNNmmdo`                         
@echo		           .dmNNm+.                          /NmNds/.``.:ohmMMdNNNNNNy.`                            
@echo		     `:+ossooo+sdNms.                         /NMMMNs//NMMMMMMNNNNNd/                               
@echo		     hMMMMMMMMNdo:dNm-                         .yNMMMNNMMMMMMNNNd+:`:.`                             
@echo		     yNNNNmmNNNMM+:NNm` .``                  ````-sNNMMMMMMNNNN+   +NNmo .`                         
@echo		     `osssso++++o.sNNN:-/hyysoo++++++++ooosssyyyy`sooohdmmmmdo-  `oNNNN/.++/-`                      
@echo		     -MMMMMMMMMNy/sNNd-m-yhhhhhhhhhhhhhhhhhhhhhhs:NNNo.        .omNNNN+`/+++++/:.                   
@echo		     `hmdhhddNMMMN`mm-oN/+oyhhhhhhhhhhhhhhhhhhhhy.yNNNNdsoooshmNNNNNh-.++++++++++/-`                
@echo		       ohhhyso//:.sNN:hN:++++syhhhhhhhhhhhhhhhhhhy-+NNNNNNNNNNNNNdo-./++++++++++++++:`              
@echo		      `NMMMMMMMMm`/Ny+Ns:+++++++oossyyyyy+shhhhhhho.NNNNNNNNhso/--:+++++++++++++++++++:`            
@echo		       `:+ssyyso/+hoomo:+++++++++++++++/: shhhhhhh:oNNNNNNN+-/++++++++++++++++++++++++++:`          
@echo		          ./++++/:+yo:/++++////::--..`  ` yhhhhhhy`dNNNNNNN./+++++++++++++++++++++++++++++-`        
@echo		                  `` ```````              yhhhhhho.NNNNNNNd`+++++++++++/+++++++++++++++++++/.       
@echo		                                          yhhhhhh//NNNNNNNy.+++++++++++:--:/+++++++++++++++++.      
@echo		                                          shhhhhh:oNNNNNNN+-+++++++++++::---`.-:/+++++++++++/-.     

@TIMEOUT 20
color 0f
cls                         
@echo RUNNING STARTUP SCRIPTS
python "C:\Users\Balaji Vyshnavy\PycharmProjects\Ramdom\venv\Scripts\extractor_separate.py"
@echo Exrtraction using python COMPLETE
python "C:\Users\Balaji Vyshnavy\PycharmProjects\Ramdom\venv\Scripts\extract_sql.py"
@echo Extraction using sql script COMPLETE
@echo RE-CALCULATING START-UP CHECKSUM
python "C:\Users\Balaji Vyshnavy\PycharmProjects\Ramdom\venv\Scripts\checksum_extractor.py"
@echo REDECLARING ROLES 
python "C:\Users\Balaji Vyshnavy\PycharmProjects\Ramdom\venv\Scripts\privileges.py"
@echo Re-applying safe settings
@PAUSE
cd "C:\Users\Balaji Vyshnavy\Desktop\dump
@echo started
mysql JS > shell.options.setPersist('history.autoSave',1)
mysql JS > shell.options.setPersist('autocomplete.nameCache,'true')
mysql JS > shell.options.setPersist('batchContinueOnError','false')
mysql JS > shell.options.setPersist('credentialStore.excludeFilters','[]')
mysql JS > shell.options.setPersist('credentialStore.helper','default')
@echo *
mysql JS > shell.options.setPersist('credentialStore.savePasswords','prompt')
mysql JS > shell.options.setPersist('dba.gtidWaitTimeout',60)
mysql JS > shell.options.setPersist('dba.logSql',2)
mysql JS > shell.options.setPersist('dba.restartWaitTimeout',60)
mysql JS > shell.options.setPersist('defaultCompress','false')
@echo *
mysql JS > shell.options.setPersist('defaultMode','sql')
mysql JS > shell.options.setPersist('devapi.dbObjectHandles','true')
mysql JS > shell.options.setPersist('history.maxSize',100000)
mysql JS > shell.options.setPersist('history.sql.ignorePattern','*IDENTIFIED*:*PASSWORD*')
mysql JS > shell.options.setPersist('logLevel',8)
@echo *
mysql JS > shell.options.setPersist('interactive','true')
mysql JS > shell.options.setPersist('oci.configFile','C:\Users\Balaji Vyshnavy\.oci\config')
mysql JS > shell.options.setPersist('oci.profile','DEFAULT')
mysql JS > shell.options.setPersist('outputFormat','table')
mysql JS > shell.options.setPersist('passwordsFromStdin','false')
@echo *
mysql JS > shell.options.setPersist('resultFormat','table')
mysql JS > shell.options.setPersist('sandboxDir','C:\Users\Balaji Vyshnavy\MySQL\mysql-sandboxes')
mysql JS > shell.options.setPersist('showColumnTypeInfo','false')
mysql JS > shell.options.setPersist('showWarnings','true')
mysql JS > shell.options.setPersist('useWizards','true')
mysql JS > shell.options.setPersist('verbose',1)
@echo *
@echo DONE!!!
@echo ready to start sql shell with safety settings
@PAUSE
mysqlsh --mysql --sql --table --verbose 1 --uri maintenance_admin@localhost:3306 --database custom1 --log-level 8 

