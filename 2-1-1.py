import torch
import torch.nn as nn

class SimpleMLP(nn.Module):
    def __init__(self,
                 vec_length:int=16,
                 hidden_unit_1:int=8,
                 hidden_unit_2:int=2):
        
        """"
        引数:
        vec_length: 入力ベクトルの長さ
        hidden_unit_1: 1つ目の線形層のニューロン数
        hidden_unit_2: 2つ目の線形層のニューロン数
        """

        #継承しているnn.Moduleの__init__()メソッドの呼び出し
        super(SimpleMLP, self).__init__()

        #1つ目の線形層
        self.layer1 = nn.Linear(vec_length, hidden_unit_1)
        #活性化関数のReLU
        self.relu   = nn.ReLU()
        #2つ目の線形層
        self.layer2 = nn.Linear(hidden_unit_1, hidden_unit_2)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        順伝播は、線形層→ReLU→線形層の順番
        引数:
            x:   入力(B, D_in)
                B: バッチサイズ、D_in: ベクトルの長さ
        
        返り値:
            out: 出力(B, D_out)
                B: バッチサイズ、D_out: ベクトルの長さ
                
        """

        #1つ目の線形層
        out = self.layer1(x)
        #ReLU
        out = self.relu(out)
        #２つ目の線形層
        out = self.layer2(out)

        return out
    
