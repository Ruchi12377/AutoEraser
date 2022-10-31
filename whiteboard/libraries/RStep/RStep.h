#ifndef RStep_h
#define RStep_h

// クラスの定義
class RStep
{
public:
    //コンストラクタ
    RStep(int pul, int dir, int ena, int round);
    //回転
    void spin(int direction, unsigned int num);
    //強制停止
    void stop();

private:
    //それぞれの制御ピン
    int m_pul;
    int m_dir;
    int m_ena;
    //1回転に必要な回転数
    unsigned int m_round;
};

#endif
