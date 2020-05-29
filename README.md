# Mlops

job 4

filename="acc.txt"

while IFS= read -r line; 
do 
if [[ $line == 0.9* ]] ;
then
printline="yes"       
echo "-----------------------"
echo "MODEL HAS TRAINED SUCESSFULLY"
echo "-----------------------"   
fi

if [[ $printline == "yes" ]] ;
then
echo "-----------------------"
echo "MODEL ACCURACY IS $line"
echo "-----------------------"         
fi  


if [[ $line == 0.6* ]] ; 
then       
printline="no"
if sudo docker ps | grep model
then
sudo docker rm -f model 
echo "MODEL REMOVED"
fi

if [[ $printline == "no" ]] 
echo "-----------------------"
echo "MODEL ACCURACY IS LESS $line"
echo "-----------------------" 
echo "TWEAKING MODEL" 

sed -i '64i model.add(Dense(units=10,activation="relu",kernel_initializer="he_normal" )) ' main.py

sudo docker run -it -v /root/ws/:/usr/src/mlops --name tuning act3:v1       
fi

if sudo docker ps | grep tuning 
then
sudo docker rm -f tuning 
echo "-----------------------"
echo "MODEL ACCURACY IS LESS AGAIN $line"
echo "-----------------------" 
echo "TWEAKING MODEL AGAIN" 

sed -i '76i model.add(Dense(units=7,activation="relu",kernel_initializer="he_normal" ))

done < "$filename"
