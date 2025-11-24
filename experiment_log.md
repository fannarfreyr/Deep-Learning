# Experiment Log

## Experiment: Baseline single head classification all layers except fc are frozen
**Date:** 2025-11-23 22:14:09

### Changes
None, this is the baseline

### Reason
Measure a baseline to compare to

### Metrics
- Epoch 1: train_loss=4.756690376425192, train_top1=8.749040675218161, train_top5=23.131235606617317, val_loss=4.186660209852468, val_top1=16.942909751222352, val_top5=40.3928790715957
- Epoch 2: train_loss=3.318053653143226, train_top1=45.80199539055755, train_top5=74.2133537883861, val_loss=3.6642330931036513, val_top1=26.826273779403657, val_top5=52.547575204192384
- Epoch 3: train_loss=2.490202739763882, train_top1=67.53645432912104, train_top5=89.37835764207935, val_loss=3.3278836059453227, val_top1=31.614487395687583, val_top5=58.37937382088621
- Epoch 4: train_loss=1.9122096590326094, train_top1=78.4036837960607, train_top5=94.52033767407433, val_loss=3.1242336076487054, val_top1=33.88581952469125, val_top5=60.589318595684844
- Epoch 5: train_loss=1.4882188129681215, train_top1=86.7996930079193, train_top5=97.65157329240215, val_loss=2.979874514157674, val_top1=36.218538984482535, val_top5=63.22897483821
- Epoch 6: train_loss=1.157973064849309, train_top1=91.972371454012, train_top5=98.87950882578664, val_loss=2.863996946423825, val_top1=37.38489869213163, val_top5=64.21117249378183
- Epoch 7: train_loss=0.9280253464866398, train_top1=94.7966231772832, train_top5=99.57022256331543, val_loss=2.781894972457558, val_top1=37.75322283960838, val_top5=65.13198281856604
- Epoch 8: train_loss=0.7499706934345565, train_top1=96.62317728904789, train_top5=99.78511128165772, val_loss=2.712803054397424, val_top1=39.472068758520194, val_top5=66.42111726858046
- Epoch 9: train_loss=0.6008788244228407, train_top1=98.25019187078234, train_top5=99.93860322333077, val_loss=2.6990522366495058, val_top1=40.27010433976822, val_top5=66.54389197699054
- Epoch 10: train_loss=0.49735733464600396, train_top1=98.98695318495778, train_top5=99.95395241749809, val_loss=2.6380398860367036, val_top1=40.085942277153116, val_top5=67.71025170688617
- Epoch 11: train_loss=0.41091016428066235, train_top1=99.38603223330774, train_top5=99.9846508058327, val_loss=2.6165183726229353, val_top1=41.74340084068903, val_top5=67.09637815312713
- Epoch 12: train_loss=0.3419807001982665, train_top1=99.5088257866462, train_top5=100.0, val_loss=2.583307102313431, val_top1=41.436464080201695, val_top5=68.13996318632141
- Epoch 13: train_loss=0.2891655498162106, train_top1=99.78511128165772, train_top5=100.0, val_loss=2.577523599598875, val_top1=40.76120318394632, val_top5=67.64886435268114
- Epoch 14: train_loss=0.24772838785478177, train_top1=99.80046047582502, train_top5=100.0, val_loss=2.542328888247392, val_top1=40.945365236023584, val_top5=68.75383672837175
- Epoch 15: train_loss=0.20891222185294445, train_top1=99.84650805832693, train_top5=100.0, val_loss=2.552252348103064, val_top1=41.19091465284372, val_top5=67.89441376950127
- hierarchical_consistency: 0.5316144874155924
- accuracy_Chrysler: 0.48333333333333334
- accuracy_Ford: 0.4897959183673469
- accuracy_Hyundai: 0.5542168674698795
- accuracy_GMC: 0.5609756097560976
- accuracy_Toyota: 0.59375
- accuracy_Chevrolet: 0.5638297872340425
- accuracy_smart: 0.625
- accuracy_Suzuki: 0.3902439024390244
- accuracy_Bentley: 0.5357142857142857
- accuracy_Dodge: 0.5535714285714286
- accuracy_Acura: 0.46938775510204084
- accuracy_Volvo: 0.4666666666666667
- accuracy_Audi: 0.6018518518518519
- accuracy_Mitsubishi: 0.16666666666666666
- accuracy_Ferrari: 0.8181818181818182
- accuracy_Jeep: 0.5116279069767442
- accuracy_Eagle: 0.5555555555555556
- accuracy_Land Rover: 0.6428571428571429
- accuracy_Mercedes-Benz: 0.509090909090909
- accuracy_BMW: 0.5363636363636364
- accuracy_Ram: 0.8333333333333334
- accuracy_Lincoln: 0.6666666666666666
- accuracy_Bugatti: 0.5833333333333334
- accuracy_Fisker: 0.1111111111111111
- accuracy_Aston Martin: 0.4230769230769231
- accuracy_Honda: 0.4482758620689655
- accuracy_Daewoo: 0.45454545454545453
- accuracy_Buick: 0.4583333333333333
- accuracy_McLaren: 0.5
- accuracy_Volkswagen: 0.37037037037037035
- accuracy_Lamborghini: 0.6326530612244898
- accuracy_Infiniti: 0.38461538461538464
- accuracy_Spyker: 0.8888888888888888
- accuracy_Plymouth: 0.75
- accuracy_HUMMER: 0.9230769230769231
- accuracy_Mazda: 0.5714285714285714
- accuracy_Cadillac: 0.26666666666666666
- accuracy_Nissan: 0.3684210526315789
- accuracy_Scion: 0.5
- accuracy_AM: 0.8
- accuracy_Jaguar: 0.2
- accuracy_Rolls-Royce: 0.42857142857142855
- accuracy_Isuzu: 0.75
- accuracy_Tesla: 0.5
- accuracy_Geo: 1.0
- accuracy_FIAT: 0.8461538461538461
- accuracy_MINI: 0.75
- accuracy_Maybach: 0.3333333333333333
- accuracy_Porsche: 0.42857142857142855

### Results
Best Top-1 Accuracy = 41.74%, Hierarchical Consistency = 0.5316


--- Starting Phase 1 Baseline Evaluation ---
Test Set Size: 8041
----------------------------------------
1. Exact Car Accuracy (Hard):  41.72%  (Target for fine-tuning)
2. Make/Brand Accuracy (Easy): 52.82%  (Target for coarse features)
----------------------------------------
3. THE GAP:                    11.09% points

### Gemini thoughts on accuracy above
1. Exact Accuracy (42%): This is your floor. Your model is getting less than half of the cars right.

2. Make Accuracy (53%): This is surprisingly low. It means that nearly half the time, the model doesn't even know it's looking at a "BMW" vs. a "Ford."

3. The Gap (11%): This proves your hypothesis: Hierarchy matters. The model is significantly better at the "Easy" task (Make) than the "Hard" task (Model), but because you are using a standard flat classifier, it isn't effectively leveraging the easy task to help solve the hard one.

### Notes
Training finished. Logged curves, confusion matrix, sample image.


### Images / Plots
![img](plots/Baseline_single_head_classification_loss_curve.png)
![img](plots/Baseline_single_head_classification_accuracy_curve.png)
![img](plots/Baseline_single_head_classification_confusion_matrix.png)
![img](plots/Baseline_single_head_classification_11_23_22_14_sample_val_image.png)

---

## Experiment: Baseline single head classification unfrozen layers
**Date:** 2025-11-23 23:39:19

### Changes
Unfroze the rest of the model parameters, previously only the fc layer at the end was unfrozen and the ImageNet layers were frozen

### Reason
The model is using generic 'ImageNet' eyes. It knows what a 'wheel' is, but it doesn't know the specific shape of a '2012 BMW headlight.' 
 The hypothesis: Exact Accuracy should jump significantly (likely to 60-70%+).

### Metrics
- Epoch 1: train_loss=4.784462774925203, train_top1=7.5057559442995885, train_top5=20.69071373665049, val_loss=3.68499265162033, val_top1=21.11724984448259, val_top5=48.31184776287419
- Epoch 2: train_loss=2.4955783588924687, train_top1=49.13277053071825, train_top5=79.18649269859331, val_loss=1.8173698773041616, val_top1=57.76550030225329, val_top5=85.63535912538907
- Epoch 3: train_loss=0.9346095656397154, train_top1=82.5786646259627, train_top5=97.19109745918561, val_loss=1.2652581198366235, val_top1=69.42909756842532, val_top5=91.7127071354856
- Epoch 4: train_loss=0.31030790766934113, train_top1=95.88641596316194, train_top5=99.73906369915579, val_loss=1.023550943848251, val_top1=74.27869855062299, val_top5=93.43155305322655
- Epoch 5: train_loss=0.11305745982108259, train_top1=99.04834995342966, train_top5=99.9846508058327, val_loss=0.9354753313509506, val_top1=76.05893190218818, val_top5=93.6771024934641
- Epoch 6: train_loss=0.045973470542902954, train_top1=99.73906369915579, train_top5=100.0, val_loss=0.8813783135276546, val_top1=78.14610194515933, val_top5=94.29097609171625
- Epoch 7: train_loss=0.024903129536089582, train_top1=99.84650805832693, train_top5=100.0, val_loss=0.8596108256855796, val_top1=78.33026400777443, val_top5=93.92265196648604
- Epoch 8: train_loss=0.016833524169516126, train_top1=99.84650805832693, train_top5=100.0, val_loss=0.8592310819324355, val_top1=77.96193988254423, val_top5=94.229588657892
- Epoch 9: train_loss=0.012860797598660679, train_top1=99.90790483499616, train_top5=100.0, val_loss=0.8550251524751358, val_top1=77.77777770752553, val_top5=94.229588657892
- Epoch 10: train_loss=0.009989426578362905, train_top1=99.90790483499616, train_top5=100.0, val_loss=0.8674976508847184, val_top1=77.53222840310899, val_top5=93.79987717845675
- Epoch 11: train_loss=0.008886432010145802, train_top1=99.87720644666155, train_top5=100.0, val_loss=0.8710677714857168, val_top1=77.65500303189984, val_top5=94.29097609171625
- Epoch 12: train_loss=0.007135792681411286, train_top1=99.89255564082886, train_top5=100.0, val_loss=0.8540685079520725, val_top1=78.33026400777443, val_top5=94.4137507205071
- Epoch 13: train_loss=0.006611056273041188, train_top1=99.89255564082886, train_top5=100.0, val_loss=0.8955176870759972, val_top1=77.22529163208382, val_top5=93.92265188686682
- Epoch 14: train_loss=0.006172642445567701, train_top1=99.87720644666155, train_top5=100.0, val_loss=0.8960173458976933, val_top1=77.59361567769481, val_top5=94.22958873751121
- Epoch 15: train_loss=0.012592953730571847, train_top1=99.7544128933231, train_top5=99.9846508058327, val_loss=1.1438741295377195, val_top1=71.51626769101568, val_top5=91.28299565605037
- hierarchical_consistency: 0.8833640270104358
- accuracy_Chrysler: 0.8833333333333333
- accuracy_Ford: 0.9183673469387755
- accuracy_Hyundai: 0.8795180722891566
- accuracy_GMC: 0.8048780487804879
- accuracy_Toyota: 0.90625
- accuracy_Chevrolet: 0.8351063829787234
- accuracy_smart: 1.0
- accuracy_Suzuki: 0.9024390243902439
- accuracy_Bentley: 0.9285714285714286
- accuracy_Dodge: 0.9285714285714286
- accuracy_Acura: 0.8163265306122449
- accuracy_Volvo: 0.8666666666666667
- accuracy_Audi: 0.9166666666666666
- accuracy_Mitsubishi: 0.75
- accuracy_Ferrari: 1.0
- accuracy_Jeep: 0.9767441860465116
- accuracy_Eagle: 0.7777777777777778
- accuracy_Land Rover: 0.9285714285714286
- accuracy_Mercedes-Benz: 0.7818181818181819
- accuracy_BMW: 0.9090909090909091
- accuracy_Ram: 1.0
- accuracy_Lincoln: 1.0
- accuracy_Bugatti: 0.9583333333333334
- accuracy_Fisker: 0.7777777777777778
- accuracy_Aston Martin: 1.0
- accuracy_Honda: 0.9310344827586207
- accuracy_Daewoo: 0.8181818181818182
- accuracy_Buick: 0.875
- accuracy_McLaren: 0.8333333333333334
- accuracy_Volkswagen: 0.8148148148148148
- accuracy_Lamborghini: 0.8775510204081632
- accuracy_Infiniti: 0.8461538461538461
- accuracy_Spyker: 0.8888888888888888
- accuracy_Plymouth: 0.875
- accuracy_HUMMER: 0.8461538461538461
- accuracy_Mazda: 1.0
- accuracy_Cadillac: 0.7666666666666667
- accuracy_Nissan: 0.8421052631578947
- accuracy_Scion: 1.0
- accuracy_AM: 0.9
- accuracy_Jaguar: 0.6666666666666666
- accuracy_Rolls-Royce: 0.8928571428571429
- accuracy_Isuzu: 1.0
- accuracy_Tesla: 1.0
- accuracy_Geo: 1.0
- accuracy_FIAT: 0.9230769230769231
- accuracy_MINI: 0.9166666666666666
- accuracy_Maybach: 0.6666666666666666
- accuracy_Porsche: 0.8571428571428571

### Results
Best Top-1 Accuracy = 78.33%, Hierarchical Consistency = 0.8834


--- Starting Phase 2 Baseline Evaluation ---
Test Set Size: 8041
----------------------------------------
1. Exact Car Accuracy (Hard):  75.92%  (Target for fine-tuning)
2. Make/Brand Accuracy (Easy): 85.49%  (Target for coarse features)
----------------------------------------
3. THE GAP:                    9.56% points

### Notes from Gemini
This is a textbook result for your report. You have successfully created a strong narrative:

1. Phase 1 (Frozen): Acc ~42%. The model was blind to specific features.

1. Phase 2 (Fine-Tuned): Acc ~76%. The model learned the specific features, BUT the "Hierarchy Gap" barely moved (dropped from 11% to 9.5%).

The Narrative for the report:

"Fine-tuning improved raw performance, but it failed to solve the structural inconsistency. The model is still significantly better at guessing the Brand than the Car, implying it is learning them as separate tasks rather than a structured hierarchy. Phase 3 (Multi-Head) is designed to explicitly link these two tasks."

### Notes
Training finished. Logged curves, confusion matrix, sample image.

### Images / Plots
![img](plots/Baseline single head classification unfrozen layers_loss_curve.png)
![img](plots/Baseline single head classification unfrozen layers_accuracy_curve.png)
![img](plots/Baseline single head classification unfrozen layers_confusion_matrix.png)
![img](plots/Baseline single head classification unfrozen layers_11_23_23_39_sample_val_image.png)

---

## Experiment: Multihead_two_heads
**Date:** 2025-11-24 18:20:10

### Changes
Added another classification head, so two in total. One head only predicts the make (Toyota, Mazda, Ford,...), The other predicts the full model label.

### Reason
We want to make sure that the model is learning the hierarchy. i.e., it at least gets better at predicting the 'easy' problem (make) and hoping for some improvement also for the 'hard' problem (full model label)

### Metrics
- Epoch 1: train_loss=7.946168717950102, train_top1=5.6792018419033, train_top5=17.405986184554198, val_loss=6.1999869121226014, val_top1=17.24984652751644, val_top5=45.365254738786014
- Epoch 2: train_loss=4.365030718545043, train_top1=43.13123561130152, train_top5=74.02916346072053, val_loss=3.2356772683309294, val_top1=51.626764902825585, val_top5=84.22344989905407
- Epoch 3: train_loss=1.7826110722738693, train_top1=75.34919416262201, train_top5=95.99386032233308, val_loss=2.116189131932876, val_top1=66.17556779555854, val_top5=90.11663592615473
- Epoch 4: train_loss=0.6796543514188765, train_top1=90.91327705295473, train_top5=99.53952417498081, val_loss=1.7306543238840635, val_top1=72.62124006670629, val_top5=92.14241869454007
- Epoch 5: train_loss=0.290493277543248, train_top1=96.89946277820414, train_top5=99.9846508058327, val_loss=1.5192235909480123, val_top1=75.32228357210856, val_top5=94.29097597931265
- Epoch 6: train_loss=0.1342286072002405, train_top1=99.21719109746738, train_top5=100.0, val_loss=1.4107489994217677, val_top1=76.55003071241103, val_top5=94.41375068772271
- Epoch 7: train_loss=0.06610052237260003, train_top1=99.70836531082118, train_top5=100.0, val_loss=1.370692363906448, val_top1=77.04112956946872, val_top5=94.65930010454285
- Epoch 8: train_loss=0.043140668175537036, train_top1=99.83115886415963, train_top5=100.0, val_loss=1.3732357099789503, val_top1=76.85696748343621, val_top5=94.72068745874788
- Epoch 9: train_loss=0.030294130302262325, train_top1=99.87720644666155, train_top5=100.0, val_loss=1.403000630067857, val_top1=77.59361567769481, val_top5=94.41375074392451
- Epoch 10: train_loss=0.024227657228571033, train_top1=99.87720644666155, train_top5=100.0, val_loss=1.353612500366951, val_top1=77.96193980292502, val_top5=94.22958862510761
- Epoch 11: train_loss=0.02020449945310035, train_top1=99.84650805832693, train_top5=100.0, val_loss=1.3687345451778836, val_top1=78.26887657395018, val_top5=94.29097597931265
- Epoch 12: train_loss=0.015681779668512752, train_top1=99.89255564082886, train_top5=100.0, val_loss=1.3449159399580561, val_top1=78.69858810958722, val_top5=94.29097603551445
- Epoch 13: train_loss=0.016340145225124184, train_top1=99.86185725249425, train_top5=100.0, val_loss=1.4388483062413955, val_top1=77.04112956946872, val_top5=93.98403926448927
- Epoch 14: train_loss=0.14596560577749748, train_top1=98.81811204911742, train_top5=99.95395241749809, val_loss=2.0433415961163113, val_top1=67.83302641529625, val_top5=90.17802333656157
- Epoch 15: train_loss=0.22840870121123694, train_top1=97.31389101252405, train_top5=99.95395241749809, val_loss=1.7162447706038708, val_top1=72.49846535829623, val_top5=91.89686927771993
- hierarchical_consistency: 0.8809085328422345
- accuracy_Chrysler: 0.9
- accuracy_Ford: 0.8979591836734694
- accuracy_Hyundai: 0.8554216867469879
- accuracy_GMC: 0.8292682926829268
- accuracy_Toyota: 0.875
- accuracy_Chevrolet: 0.824468085106383
- accuracy_smart: 1.0
- accuracy_Suzuki: 0.7073170731707317
- accuracy_Bentley: 0.9285714285714286
- accuracy_Dodge: 0.8839285714285714
- accuracy_Acura: 0.8775510204081632
- accuracy_Volvo: 0.9
- accuracy_Audi: 0.8981481481481481
- accuracy_Mitsubishi: 0.75
- accuracy_Ferrari: 0.9545454545454546
- accuracy_Jeep: 0.9302325581395349
- accuracy_Eagle: 0.7777777777777778
- accuracy_Land Rover: 0.9285714285714286
- accuracy_Mercedes-Benz: 0.8181818181818182
- accuracy_BMW: 0.9363636363636364
- accuracy_Ram: 1.0
- accuracy_Lincoln: 0.8888888888888888
- accuracy_Bugatti: 0.9583333333333334
- accuracy_Fisker: 0.7777777777777778
- accuracy_Aston Martin: 1.0
- accuracy_Honda: 0.9310344827586207
- accuracy_Daewoo: 0.9090909090909091
- accuracy_Buick: 0.875
- accuracy_McLaren: 1.0
- accuracy_Volkswagen: 0.9259259259259259
- accuracy_Lamborghini: 0.9183673469387755
- accuracy_Infiniti: 0.9230769230769231
- accuracy_Spyker: 0.8888888888888888
- accuracy_Plymouth: 0.875
- accuracy_HUMMER: 0.8461538461538461
- accuracy_Mazda: 0.7142857142857143
- accuracy_Cadillac: 0.8666666666666667
- accuracy_Nissan: 0.8421052631578947
- accuracy_Scion: 1.0
- accuracy_AM General: 1.0
- accuracy_Jaguar: 0.8666666666666667
- accuracy_Rolls-Royce: 0.8571428571428571
- accuracy_Isuzu: 1.0
- accuracy_Tesla: 1.0
- accuracy_Geo: 1.0
- accuracy_FIAT: 0.9230769230769231
- accuracy_MINI: 0.8333333333333334
- accuracy_Maybach: 0.8333333333333334
- accuracy_Porsche: 0.7142857142857143

### Top-1 Accuracy per Epoch
[5.6792018419033, 17.24984652751644, 43.13123561130152, 51.626764902825585, 75.34919416262201, 66.17556779555854, 90.91327705295473, 72.62124006670629, 96.89946277820414, 75.32228357210856, 99.21719109746738, 76.55003071241103, 99.70836531082118, 77.04112956946872, 99.83115886415963, 76.85696748343621, 99.87720644666155, 77.59361567769481, 99.87720644666155, 77.96193980292502, 99.84650805832693, 78.26887657395018, 99.89255564082886, 78.69858810958722, 99.86185725249425, 77.04112956946872, 98.81811204911742, 67.83302641529625, 97.31389101252405, 72.49846535829623]

### Top-5 Accuracy per Epoch
[17.405986184554198, 45.365254738786014, 74.02916346072053, 84.22344989905407, 95.99386032233308, 90.11663592615473, 99.53952417498081, 92.14241869454007, 99.9846508058327, 94.29097597931265, 100.0, 94.41375068772271, 100.0, 94.65930010454285, 100.0, 94.72068745874788, 100.0, 94.41375074392451, 100.0, 94.22958862510761, 100.0, 94.29097597931265, 100.0, 94.29097603551445, 100.0, 93.98403926448927, 99.95395241749809, 90.17802333656157, 99.95395241749809, 91.89686927771993]

### Results
Best Top-1 Accuracy = 78.70%, Hierarchical Consistency = 0.8809

--- Starting Phase 3 (Multi-Head) Evaluation ---
Test Set Size: 8041
----------------------------------------
1. Model Head Accuracy:    77.20% (The Hard Task)
2. Make Head Accuracy:     85.51% (The Easy Task)
----------------------------------------
3. THE GAP:                8.31% points
4. Internal Consistency:   90.44% (How often heads agree)

### Notes from Gemini

1. Why did Exact Accuracy go up? (75.9% $\to$ 77.2%) By forcing the model to answer "What Brand is this?", you gave the shared backbone (the ResNet feature extractor) a strong hint. It learned features that are distinct to specific brands (like BMW grilles or Porsche headlights) which helped the specific Car classifier do its job better. This is called Auxiliary Task Learning.
2. Why is Consistency only 90%? This is the "Frankenstein Problem." In ~9.5% of your test set (approx. 760 images), your model is confused.Head 1 says: "This is a Toyota."Head 2 says: "This is a Honda Civic."Currently, your loss function (loss_make + loss_model) treats these as separate problems. It doesn't strictly punish the model for disagreeing with itself.

### Notes
Training finished. Logged curves, confusion matrix, sample image.

### Images / Plots
![img](plots/Multihead_two_heads_loss_curve.png)
![img](plots/Multihead_two_heads_accuracy_curve.png)
![img](plots/Multihead_two_heads_11_24_18_19_confusion_matrix.png)
![img](plots/Multihead_two_heads_11_24_18_20_sample_val_image.png)

---

