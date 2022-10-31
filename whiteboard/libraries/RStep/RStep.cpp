#include "Arduino.h"
#include "RStep.h"

// コンストラクタ（初期化処理）
RStep::RStep(int pul, int dir, int ena, int round)
{
    m_pul = pul;
    m_dir = dir;
    m_ena = ena;
    m_round = round;
    pinMode(m_pul, OUTPUT);
    pinMode(m_dir, OUTPUT);
    pinMode(m_ena, OUTPUT);
}

void RStep::spin(int direction, unsigned int num)
{
    digitalWrite(m_ena, HIGH);
    if (direction == 0)
    {
        digitalWrite(m_dir, LOW);
    }
    else
    {
        digitalWrite(m_dir, HIGH);
    }

    for (int i = 0; i < num * m_round; i++)
    {
        digitalWrite(m_pul, HIGH);
        delayMicroseconds(50);
        digitalWrite(m_pul, LOW);
        delayMicroseconds(50);
    }
    digitalWrite(m_ena, LOW);
}

void RStep::stop(void)
{
}
