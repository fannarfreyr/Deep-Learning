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

## Experiment: Multihead_two_heads_with_data_augmentation
**Date:** 2025-11-25 00:45:30

### Changes
Added data augmentation

### Reason
Try to prevent the model from overfitting, and force the network to learn more robust features that remain consistent regardless of position or lighting

### Metrics
- Epoch 1: train_loss=7.815932121408599, train_top1=6.3545663851183924, train_top5=18.633921712083442, val_loss=5.869649592025504, val_top1=17.127071824375292, val_top5=49.23265805604488
- Epoch 2: train_loss=4.440406470543956, train_top1=37.20644665745159, train_top5=71.26630851646067, val_loss=2.9865334792104945, val_top1=53.77532227892609, val_top5=86.12645798244675
- Epoch 3: train_loss=2.2660845409241075, train_top1=65.74059861388832, train_top5=91.98772064466615, val_loss=1.8759257547543633, val_top1=69.24493555030331, val_top5=92.63351747197854
- Epoch 4: train_loss=1.3119086706903653, train_top1=78.91020721177915, train_top5=97.03760553156515, val_loss=1.3241887091126743, val_top1=76.55003067962666, val_top5=95.94843462246777
- Epoch 5: train_loss=0.8161561346932366, train_top1=86.44666155612386, train_top5=99.07904834176428, val_loss=1.307684128345925, val_top1=76.79558009644678, val_top5=95.58011041761836
- Epoch 6: train_loss=0.5526671981774928, train_top1=91.22026093395874, train_top5=99.58557175748273, val_loss=0.9327849331920757, val_top1=83.67096376741057, val_top5=97.23756898115427
- Epoch 7: train_loss=0.4003552406271512, train_top1=93.04681503401294, train_top5=99.84650805832693, val_loss=0.9303494195692228, val_top1=83.30263960939598, val_top5=96.86924493554328
- Epoch 8: train_loss=0.2971951404353425, train_top1=95.37989256149608, train_top5=99.92325402916347, val_loss=0.7951233823508701, val_top1=84.03928783643897, val_top5=97.60589310638447
- Epoch 9: train_loss=0.24003008695538008, train_top1=96.1627014499761, train_top5=99.96930161166539, val_loss=0.790080186375231, val_top1=85.1442602917488, val_top5=97.29895641497852
- Epoch 10: train_loss=0.2039741998142402, train_top1=96.93016116653875, train_top5=100.0, val_loss=0.7779739049404512, val_top1=84.83732354414104, val_top5=97.97421728781647
- Epoch 11: train_loss=0.16267433200354586, train_top1=97.55947812739831, train_top5=99.9846508058327, val_loss=0.8212023883454268, val_top1=85.20564764595383, val_top5=97.72866781479453
- Epoch 12: train_loss=0.1468852491810609, train_top1=97.78971604576316, train_top5=99.96930161166539, val_loss=0.7591619299115251, val_top1=84.59177402428428, val_top5=97.91282995702885
- Epoch 13: train_loss=0.11502583502625284, train_top1=98.26554105089704, train_top5=100.0, val_loss=0.6912202439548195, val_top1=86.6175567926696, val_top5=97.79005524861878
- Epoch 14: train_loss=0.10746147307129156, train_top1=98.37298541006818, train_top5=100.0, val_loss=0.7455345008766966, val_top1=85.20564764595383, val_top5=97.79005522520137
- Epoch 15: train_loss=0.10319699632005333, train_top1=98.5264773599386, train_top5=99.9846508058327, val_loss=0.739026231623779, val_top1=86.18784525703256, val_top5=97.97421723161467
- hierarchical_consistency: 0.94536525475752
- accuracy_Chrysler: 0.9166666666666666
- accuracy_Ford: 0.9183673469387755
- accuracy_Hyundai: 0.9397590361445783
- accuracy_GMC: 0.9512195121951219
- accuracy_Toyota: 0.9375
- accuracy_Chevrolet: 0.9202127659574468
- accuracy_smart: 1.0
- accuracy_Suzuki: 0.926829268292683
- accuracy_Bentley: 1.0
- accuracy_Dodge: 0.9464285714285714
- accuracy_Acura: 0.9795918367346939
- accuracy_Volvo: 0.9
- accuracy_Audi: 0.9259259259259259
- accuracy_Mitsubishi: 0.8333333333333334
- accuracy_Ferrari: 0.9545454545454546
- accuracy_Jeep: 0.9767441860465116
- accuracy_Eagle: 0.7777777777777778
- accuracy_Land Rover: 1.0
- accuracy_Mercedes-Benz: 0.9272727272727272
- accuracy_BMW: 0.9818181818181818
- accuracy_Ram: 1.0
- accuracy_Lincoln: 1.0
- accuracy_Bugatti: 1.0
- accuracy_Fisker: 0.8888888888888888
- accuracy_Aston Martin: 1.0
- accuracy_Honda: 0.9655172413793104
- accuracy_Daewoo: 1.0
- accuracy_Buick: 0.9583333333333334
- accuracy_McLaren: 1.0
- accuracy_Volkswagen: 0.8888888888888888
- accuracy_Lamborghini: 0.9591836734693877
- accuracy_Infiniti: 1.0
- accuracy_Spyker: 1.0
- accuracy_Plymouth: 1.0
- accuracy_HUMMER: 0.9230769230769231
- accuracy_Mazda: 1.0
- accuracy_Cadillac: 0.9666666666666667
- accuracy_Nissan: 1.0
- accuracy_Scion: 1.0
- accuracy_AM General: 0.9
- accuracy_Jaguar: 0.6
- accuracy_Rolls-Royce: 0.9642857142857143
- accuracy_Isuzu: 1.0
- accuracy_Tesla: 1.0
- accuracy_Geo: 1.0
- accuracy_FIAT: 1.0
- accuracy_MINI: 0.9166666666666666
- accuracy_Maybach: 1.0
- accuracy_Porsche: 1.0

### Top-1 Accuracy per Epoch
[6.3545663851183924, 17.127071824375292, 37.20644665745159, 53.77532227892609, 65.74059861388832, 69.24493555030331, 78.91020721177915, 76.55003067962666, 86.44666155612386, 76.79558009644678, 91.22026093395874, 83.67096376741057, 93.04681503401294, 83.30263960939598, 95.37989256149608, 84.03928783643897, 96.1627014499761, 85.1442602917488, 96.93016116653875, 84.83732354414104, 97.55947812739831, 85.20564764595383, 97.78971604576316, 84.59177402428428, 98.26554105089704, 86.6175567926696, 98.37298541006818, 85.20564764595383, 98.5264773599386, 86.18784525703256]

### Top-5 Accuracy per Epoch
[18.633921712083442, 49.23265805604488, 71.26630851646067, 86.12645798244675, 91.98772064466615, 92.63351747197854, 97.03760553156515, 95.94843462246777, 99.07904834176428, 95.58011041761836, 99.58557175748273, 97.23756898115427, 99.84650805832693, 96.86924493554328, 99.92325402916347, 97.60589310638447, 99.96930161166539, 97.29895641497852, 100.0, 97.97421728781647, 99.9846508058327, 97.72866781479453, 99.96930161166539, 97.91282995702885, 100.0, 97.79005524861878, 100.0, 97.79005522520137, 99.9846508058327, 97.97421723161467]

### Results
Best Top-1 Accuracy = 86.62%, Hierarchical Consistency = 0.9454

--- Starting Phase 4 (Multi-Head + Data Augmentation) Evaluation ---
Test Set Size: 8041
----------------------------------------
1. Model Head Accuracy:    85.65% (The Hard Task)
2. Make Head Accuracy:     92.71% (The Easy Task)
----------------------------------------
3. THE GAP:                7.06% points
4. Internal Consistency:   95.26% (How often heads agree)


### Notes from Gemini
1. The "Ceiling" was Shattered (Make Acc: 85% $\to$ 92%)Remember how in Phase 3 we were worried that "Make Accuracy" was stuck at 85%?Hypothesis: We thought the ResNet backbone had hit its capacity.Correction: It wasn't capacity; it was overfitting. The model had memorized the "clean" images perfectly but failed on slight variations. Data Augmentation forced it to learn robust features (like the shape of a grille regardless of angle), which instantly unlocked that extra 7% accuracy.
2. The "Free Lunch" (Model Acc: +8.45%)You gained nearly 8.5% accuracy on the hardest task without changing your architecture or training longer. This demonstrates why Data Augmentation is standard practice in Deep Learning: it converts "memorization" into "generalization."
3. Consistency Improved Automatically (90% $\to$ 95%)Interestingly, your consistency error was cut in half (from ~10% to ~5%).Why? When the model is more confident and robust about the image features, its two heads naturally agree more often. The "confused" cases (where Head 1 says Ford and Head 2 says Civic) usually happen on "weird" images. Augmentation made the model less confused by "weird" images.

### Notes
Training finished. Logged curves, confusion matrix, sample image.

### Images / Plots
![img](plots/Multihead_two_heads_with_data_augmentation_loss_curve.png)
![img](plots/Multihead_two_heads_with_data_augmentation_accuracy_curve.png)
![img](plots/Multihead_two_heads_with_data_augmentation_11_25_00_45_confusion_matrix.png)
![img](plots/Multihead_two_heads_with_data_augmentation_11_25_00_45_sample_val_image.png)

---

## Experiment: Multihead_two_heads_with_da_and_class_balancing
**Date:** 2025-11-25 13:33:46

### Changes
Weighted the rarer classes so that the model doesn't ignore those

### Reason
Want the model to perform better on rarer classes

### Metrics
- Epoch 1: train_loss=7.772945845538803, train_top1=6.630851880129904, train_top5=19.984650801734016, val_loss=5.8928094085847915, val_top1=21.731123384483904, val_top5=53.713934901303645
- Epoch 2: train_loss=4.329586911146584, train_top1=39.80046047465397, train_top5=73.29240213834773, val_loss=2.8823960661668586, val_top1=53.65254757051603, val_top5=86.2492326112376
- Epoch 3: train_loss=2.1918791427304902, train_top1=65.90943974738659, train_top5=92.47889485801996, val_loss=1.7251405352972415, val_top1=70.59545735452276, val_top5=93.61571519546088
- Epoch 4: train_loss=1.2835763503657975, train_top1=78.26554105441019, train_top5=97.42133537989255, val_loss=1.2396522223254227, val_top1=77.10251686747196, val_top5=96.31675872428056
- Epoch 5: train_loss=0.8304193948656435, train_top1=86.32386798639071, train_top5=98.89485801995396, val_loss=1.0214327933087242, val_top1=79.98772249169113, val_top5=96.62369551872314
- Epoch 6: train_loss=0.5426363576675322, train_top1=91.03607060980632, train_top5=99.6162701516726, val_loss=0.8855045299137787, val_top1=82.93431546074837, val_top5=97.60589310638447
- Epoch 7: train_loss=0.4036317541612082, train_top1=93.04681504806554, train_top5=99.86185725249425, val_loss=0.7910063673631774, val_top1=85.32842227474468, val_top5=97.97421723161467
- Epoch 8: train_loss=0.2948092286621527, train_top1=94.6738296157474, train_top5=99.86185725249425, val_loss=0.783593826238329, val_top1=85.02148560675614, val_top5=98.09699201964395
- Epoch 9: train_loss=0.2090779694633491, train_top1=96.4389869449876, train_top5=100.0, val_loss=0.7316315949804729, val_top1=86.43339469727012, val_top5=98.03560466543892
- Epoch 10: train_loss=0.18019591937683585, train_top1=97.160399070851, train_top5=99.9846508058327, val_loss=0.7785721142245188, val_top1=85.57397173839965, val_top5=97.85144260282382
- Epoch 11: train_loss=0.1562585013720592, train_top1=97.49808134253173, train_top5=100.0, val_loss=0.7829474898259869, val_top1=86.86310617670536, val_top5=97.79005524861878
- Epoch 12: train_loss=0.11472011142205205, train_top1=98.41903299257011, train_top5=100.0, val_loss=0.7498618792982611, val_top1=86.43339464106832, val_top5=97.79005524861878
- Epoch 13: train_loss=0.12925078234737503, train_top1=98.2655410590944, train_top5=99.9846508058327, val_loss=0.8652982929134896, val_top1=83.97790048223393, val_top5=96.93063221012909
- Epoch 14: train_loss=0.1459440808385862, train_top1=98.11204911742134, train_top5=99.9846508058327, val_loss=0.814074766350495, val_top1=85.02148558333873, val_top5=97.60589318600368
- Epoch 15: train_loss=0.12628492799431018, train_top1=98.35763621590088, train_top5=99.9846508058327, val_loss=0.8279479582519016, val_top1=84.71454881231357, val_top5=97.97421731123389
- hierarchical_consistency: 0.9459791282995703
- accuracy_Chrysler: 0.95
- accuracy_Ford: 0.9387755102040817
- accuracy_Hyundai: 0.963855421686747
- accuracy_GMC: 0.9024390243902439
- accuracy_Toyota: 0.9375
- accuracy_Chevrolet: 0.9042553191489362
- accuracy_smart: 1.0
- accuracy_Suzuki: 0.926829268292683
- accuracy_Bentley: 1.0
- accuracy_Dodge: 0.9553571428571429
- accuracy_Acura: 0.9795918367346939
- accuracy_Volvo: 0.9
- accuracy_Audi: 0.9722222222222222
- accuracy_Mitsubishi: 0.5833333333333334
- accuracy_Ferrari: 1.0
- accuracy_Jeep: 0.9534883720930233
- accuracy_Eagle: 0.8888888888888888
- accuracy_Land Rover: 1.0
- accuracy_Mercedes-Benz: 0.9454545454545454
- accuracy_BMW: 0.9727272727272728
- accuracy_Ram: 1.0
- accuracy_Lincoln: 1.0
- accuracy_Bugatti: 1.0
- accuracy_Fisker: 1.0
- accuracy_Aston Martin: 0.9615384615384616
- accuracy_Honda: 0.9655172413793104
- accuracy_Daewoo: 1.0
- accuracy_Buick: 0.9583333333333334
- accuracy_McLaren: 1.0
- accuracy_Volkswagen: 0.9259259259259259
- accuracy_Lamborghini: 0.9183673469387755
- accuracy_Infiniti: 0.9230769230769231
- accuracy_Spyker: 1.0
- accuracy_Plymouth: 0.875
- accuracy_HUMMER: 1.0
- accuracy_Mazda: 1.0
- accuracy_Cadillac: 0.9333333333333333
- accuracy_Nissan: 0.9473684210526315
- accuracy_Scion: 0.8333333333333334
- accuracy_AM General: 0.9
- accuracy_Jaguar: 0.8
- accuracy_Rolls-Royce: 1.0
- accuracy_Isuzu: 1.0
- accuracy_Tesla: 1.0
- accuracy_Geo: 1.0
- accuracy_FIAT: 1.0
- accuracy_MINI: 0.9166666666666666
- accuracy_Maybach: 0.6666666666666666
- accuracy_Porsche: 1.0

### Top-1 Accuracy per Epoch
[6.630851880129904, 21.731123384483904, 39.80046047465397, 53.65254757051603, 65.90943974738659, 70.59545735452276, 78.26554105441019, 77.10251686747196, 86.32386798639071, 79.98772249169113, 91.03607060980632, 82.93431546074837, 93.04681504806554, 85.32842227474468, 94.6738296157474, 85.02148560675614, 96.4389869449876, 86.43339469727012, 97.160399070851, 85.57397173839965, 97.49808134253173, 86.86310617670536, 98.41903299257011, 86.43339464106832, 98.2655410590944, 83.97790048223393, 98.11204911742134, 85.02148558333873, 98.35763621590088, 84.71454881231357]

### Top-5 Accuracy per Epoch
[19.984650801734016, 53.713934901303645, 73.29240213834773, 86.2492326112376, 92.47889485801996, 93.61571519546088, 97.42133537989255, 96.31675872428056, 98.89485801995396, 96.62369551872314, 99.6162701516726, 97.60589310638447, 99.86185725249425, 97.97421723161467, 99.86185725249425, 98.09699201964395, 100.0, 98.03560466543892, 99.9846508058327, 97.85144260282382, 100.0, 97.79005524861878, 100.0, 97.79005524861878, 99.9846508058327, 96.93063221012909, 99.9846508058327, 97.60589318600368, 99.9846508058327, 97.97421731123389]

### Results
Best Top-1 Accuracy = 86.86%, Hierarchical Consistency = 0.9460

--- Starting Phase 5 (Multi-Head with DA and Class Balancing) Evaluation ---
Test Set Size: 8041
----------------------------------------
1. Model Head Accuracy:    86.02% (The Hard Task)
2. Make Head Accuracy:     91.77% (The Easy Task)
----------------------------------------
3. THE GAP:                5.75% points
4. Internal Consistency:   94.42% (How often heads agree)

### Notes from Gemini
The Trade-off Analysis (Crucial for your Report)
You might notice that while your Model Accuracy went up (85.65% $\to$ 86.02%), your Make Accuracy and Consistency actually dropped slightly.
Why did this happen?This is the "Robin Hood Effect" of Class Balancing.
    - Before: The model ignored rare cars to maximize its score on common cars (like Fords and Toyotas). Since Fords are easy to recognize, consistency was high.
    - After: You forced the model to care about rare cars (like a "Spyker"). These are harder to recognize. By paying attention to them, the model takes more risks, leading to a slight drop in "easy" consistency but a net gain in "hard" truth.

### Notes
Training finished. Logged curves, confusion matrix, sample image.

### Images / Plots
![img](plots/Multihead_two_heads_with_da_and_class_balancing_loss_curve.png)
![img](plots/Multihead_two_heads_with_da_and_class_balancing_accuracy_curve.png)
![img](plots/Multihead_two_heads_with_da_and_class_balancing_11_25_13_33_confusion_matrix.png)
![img](plots/Multihead_two_heads_with_da_and_class_balancing_11_25_13_33_sample_val_image.png)

---

## Experiment: 3_head
**Date:** 2025-11-26 16:28:15

### Changes
Added a third head so it goes Make -> Type -> Model

### Reason
Hope the extra hierarchical layer will result in better accuracy

### Metrics
- Epoch 1: train_loss=9.32982631962938, train_top1=5.479662314215168, train_top5=18.311588642767365, val_loss=6.753651829714275, val_top1=17.004297115965223, val_top5=51.07427867048719
- Epoch 2: train_loss=5.447631686262597, train_top1=35.79432079991467, train_top5=71.17421335731208, val_loss=3.651865949507796, val_top1=53.52977287147292, val_top5=86.67894414687464
- Epoch 3: train_loss=2.9802512098987197, train_top1=64.34382194759108, train_top5=92.07981581552525, val_loss=2.3503097182332993, val_top1=67.03499076379597, val_top5=94.10681391669755
- Epoch 4: train_loss=1.8044331827990752, train_top1=77.92785879326891, train_top5=96.94551036070607, val_loss=1.7932930914736585, val_top1=75.0153468572852, val_top5=95.64149782802518
- Epoch 5: train_loss=1.142799296108284, train_top1=85.81734458706696, train_top5=98.80276285495012, val_loss=1.448771838983778, val_top1=79.25107420844634, val_top5=96.68508284951076
- Epoch 6: train_loss=0.7961056835543442, train_top1=90.11511896211005, train_top5=99.64696853415195, val_loss=1.1947278803736978, val_top1=83.97790053843573, val_top5=97.36034368956433
- Epoch 7: train_loss=0.5834485125011055, train_top1=92.34075211636944, train_top5=99.80046047582502, val_loss=1.1793689951712256, val_top1=83.6709638142454, val_top5=97.85144260282382
- Epoch 8: train_loss=0.4582695790098341, train_top1=94.19800460475825, train_top5=99.89255564082886, val_loss=1.067003707932577, val_top1=85.38980967578455, val_top5=97.97421723161467
- Epoch 9: train_loss=0.35099240009910954, train_top1=95.64082886234029, train_top5=99.9846508058327, val_loss=1.01846350951748, val_top1=87.23143035813736, val_top5=98.09699194002474
- Epoch 10: train_loss=0.2784007107351527, train_top1=96.86876437933007, train_top5=99.96930161166539, val_loss=1.0288913786374696, val_top1=86.37200731964766, val_top5=98.03560466543892
- Epoch 11: train_loss=0.24347815458260402, train_top1=97.11435150240169, train_top5=99.9846508058327, val_loss=1.0015777904172116, val_top1=85.88090850942481, val_top5=98.0356045858197
- Epoch 12: train_loss=0.20427650777724551, train_top1=97.72831926323867, train_top5=100.0, val_loss=1.0120459231516568, val_top1=86.61755681608702, val_top5=98.0356045858197
- Epoch 13: train_loss=0.16581672369999237, train_top1=98.15809669992325, train_top5=100.0, val_loss=0.9565192327095439, val_top1=87.23143030193556, val_top5=98.52670349907919
- Epoch 14: train_loss=0.18332641928907734, train_top1=98.03530314658481, train_top5=99.96930161166539, val_loss=0.9950707791552652, val_top1=86.2492326112376, val_top5=97.79005522520137
- Epoch 15: train_loss=0.17072010723701003, train_top1=98.3883346042355, train_top5=100.0, val_loss=1.046798050147467, val_top1=86.37200735243205, val_top5=97.91282995702885
- hierarchical_consistency: 0.02394106813996317
- accuracy_Chrysler: 0.0
- accuracy_Ford: 0.0
- accuracy_Hyundai: 0.0
- accuracy_GMC: 0.0
- accuracy_Toyota: 0.0
- accuracy_Chevrolet: 0.0
- accuracy_smart: 0.0
- accuracy_Suzuki: 0.0
- accuracy_Bentley: 0.0
- accuracy_Dodge: 0.0
- accuracy_Acura: 0.7959183673469388
- accuracy_Volvo: 0.0
- accuracy_Audi: 0.0
- accuracy_Mitsubishi: 0.0
- accuracy_Ferrari: 0.0
- accuracy_Jeep: 0.0
- accuracy_Eagle: 0.0
- accuracy_Land Rover: 0.0
- accuracy_Mercedes-Benz: 0.0
- accuracy_BMW: 0.0
- accuracy_Ram: 0.0
- accuracy_Lincoln: 0.0
- accuracy_Bugatti: 0.0
- accuracy_Fisker: 0.0
- accuracy_Aston Martin: 0.0
- accuracy_Honda: 0.0
- accuracy_Daewoo: 0.0
- accuracy_Buick: 0.0
- accuracy_McLaren: 0.0
- accuracy_Volkswagen: 0.0
- accuracy_Lamborghini: 0.0
- accuracy_Infiniti: 0.0
- accuracy_Spyker: 0.0
- accuracy_Plymouth: 0.0
- accuracy_HUMMER: 0.0
- accuracy_Mazda: 0.0
- accuracy_Cadillac: 0.0
- accuracy_Nissan: 0.0
- accuracy_Scion: 0.0
- accuracy_AM General: 0.0
- accuracy_Jaguar: 0.0
- accuracy_Rolls-Royce: 0.0
- accuracy_Isuzu: 0.0
- accuracy_Tesla: 0.0
- accuracy_Geo: 0.0
- accuracy_FIAT: 0.0
- accuracy_MINI: 0.0
- accuracy_Maybach: 0.0
- accuracy_Porsche: 0.0

### Top-1 Accuracy per Epoch
[5.479662314215168, 17.004297115965223, 35.79432079991467, 53.52977287147292, 64.34382194759108, 67.03499076379597, 77.92785879326891, 75.0153468572852, 85.81734458706696, 79.25107420844634, 90.11511896211005, 83.97790053843573, 92.34075211636944, 83.6709638142454, 94.19800460475825, 85.38980967578455, 95.64082886234029, 87.23143035813736, 96.86876437933007, 86.37200731964766, 97.11435150240169, 85.88090850942481, 97.72831926323867, 86.61755681608702, 98.15809669992325, 87.23143030193556, 98.03530314658481, 86.2492326112376, 98.3883346042355, 86.37200735243205]

### Top-5 Accuracy per Epoch
[18.311588642767365, 51.07427867048719, 71.17421335731208, 86.67894414687464, 92.07981581552525, 94.10681391669755, 96.94551036070607, 95.64149782802518, 98.80276285495012, 96.68508284951076, 99.64696853415195, 97.36034368956433, 99.80046047582502, 97.85144260282382, 99.89255564082886, 97.97421723161467, 99.9846508058327, 98.09699194002474, 99.96930161166539, 98.03560466543892, 99.9846508058327, 98.0356045858197, 100.0, 98.0356045858197, 100.0, 98.52670349907919, 99.96930161166539, 97.79005522520137, 100.0, 97.91282995702885]

### Results
Best Top-1 Accuracy = 87.23%, Hierarchical Consistency = 0.0239

--- Starting Phase 6 (3-Head) Evaluation ---
Test Set Size: 8041
----------------------------------------
1. Model Head Accuracy:    85.36% (The Hard Task)
2. Type Head Accuracy:     93.06% (The Medium Task)
3. Make Head Accuracy:     91.94% (The Easy Task)
----------------------------------------
4. Make-Model Consistency:   94.44% (Brand Matches Car)
5. Type-Model Consistency:   94.98% (Type Matches Car)
----------------------------------------
Make-Gap:  6.58%
Type-Gap:   7.70%

### Notes from Gemini

1. The "Task Interference" PhenomenonYour Hard Accuracy (Model) dropped slightly: 86.02% $\to$ 85.36%.
    - Why? You added a third boss (the "Type" head). Now the ResNet backbone is trying to satisfy three different masters at the same time from Epoch 0.
    - The Conflict: The gradients from the "Type" loss are pulling the weights one way (focus on shape), while the "Make" loss pulls another (focus on logos/grilles), and the "Model" loss pulls a third. This "noise" early in training prevented the backbone from fine-tuning the Model features as perfectly as before.
2. The "Type" Hypothesis was Correct
    Your Type Accuracy (93.06%) is higher than your Make Accuracy (91.94%).
    - Interpretation: It is easier for the model to see that a car is a "Sedan" (Type) than to see it is a "Ford" (Make).
    - Strategic Value: This proves that "Type" is the perfect Intermediate Scaffolding. If you teach the model "Type" first (via Curriculum Learning), you build a massive, stable foundation of features that the "Model Head" can later use to get that score back above 86%.

### Notes
Training finished. Logged curves, confusion matrix, sample image.

### Images / Plots
![img](plots/3_head_loss_curve.png)
![img](plots/3_head_accuracy_curve.png)
![img](plots/3_head_11_26_16_27_confusion_matrix.png)
![img](plots/3_head_11_26_16_28_sample_val_image.png)

---

