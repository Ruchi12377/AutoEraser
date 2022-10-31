#include <RStep.h>

RStep v = RStep(12, 11, 10, 1, 0, 1550);
RStep v2 = RStep(9, 8, 7, 0, 0, 1550);
RStep h = RStep(6, 5, 4, 1, 0, 1550);

int split(String data, char delimiter, String *dst){
    int index = 0;
    int arraySize = (sizeof(data)/sizeof((data)[0]));  
    int datalength = data.length();
    for (int i = 0; i < datalength; i++) {
        char tmp = data.charAt(i);
        if ( tmp == delimiter ) {
            index++;
            if ( index > (arraySize - 1)) return -1;
        }
        else dst[index] += tmp;
    }
    return (index + 1);
}
 
void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop()
{
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
  return;
  h.update();
  v.update();
  v2.update();

  while (Serial.available() != 0)
  {
    String str = Serial.readString();
    str.trim();
    if(str == "stop"){
      h.stop();
      v.stop();
      v2.stop();
    }

    String cmds[3] = {"\0"}; // 分割された文字列を格納する配列 
    int index = split(str, ':', cmds);
    long hNum = cmds[0].toInt();
    h.set(hNum);
    long vNum = cmds[1].toInt();
    v.set(vNum);
    v2.set(vNum);
  }
}
