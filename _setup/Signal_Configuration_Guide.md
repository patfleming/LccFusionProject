---
title: Signal Configuration Planning
typora-root-url: ..
layout: default
permalink: /:name/
nav_order: 3
use_cases:
  - Learning & Planning
  - Signaling Systems
---

# Signal Configuration Overview {#signal-configuration-planning}

In this section, we delve into the intricacies of signal planning, focusing on the configuration of signal aspects rather than the physical setup of signal masts and lamps. Here, we outline various configurations of signal mast heads and lamps and detail the downstream elements that govern signal aspects.

By focusing on signal aspects and the logic underlying their configuration, this guide aims to equip you with the tools necessary for effective signal planning on your model railroad.

Setting signal aspects is configured by define one or more logics, which check for downstream conditions and perform actions to set the signal aspects.  During planning, we show a logic statement using the following form: 

<Logic statements follow the format: **IF** (conditional) **THEN** *action(s) for true conditions* **ELSE** *actions for false conditions*> 

Multiple logic statements are grouped together into **Signal Group** to support complex configurations; multiple headed signals and when checking blocks, main routes, divergent routes, and other downstream signals.

## Terminology

Below is a set of terms used in both planning and configuring of signal aspects:

- **Logic Statement**: for planning purposes, a logic statement is in the form of an typical *if-then-else* statements as shown here: 

  **IF** `conditional` **THEN** ``action(s) for true conditions`` **ELSE** `actions for false conditions` 

  Example: 1. **If** Block is Occupied, **Then** Set aspect to `Stop` and `Exit` **Else** Set aspect to `Clear` and `Continue`.

  Explanation: 

  ```
  - `1.`: indicates this is the first logic statement in the group.
  - `Block is Occupied`: is the conditional, consisting of a single variable to be check for true or false.  Up to two variables can be specified, seperated by a logic operator like `OR`,  and `AND`
  - `Set aspect to Stop`  is the action that to be performed when the conditional is true.
  - `Continue` determines that the processing of additonal logics should continue.  If this is the last (or only) logic statement in the group, then processing of the group will stop and proceed with the next logic group.
  - `Set aspect to Clear` is the action to be performed when the conditional is false.  
  ```

- **Conditionals**: condition(s) to be evaluated, resulting in either true or false.  Conditionals contain either one or two variables.  When two variables are define, a logic operator is used; `V1 and V2`, `V1 OR V2`, `V1 Only`, etc.

- **Actions**: is what happens when the conditional is *true* or *false*.  Typically the action *sets the aspect* or does nothing.

- **Logic Group**: represents a collection of logic configurations accessible via the CDI tool in the **Logics and Conditionals** section. 

  - Planning example: 
    1. **If** Block is Occupied, **Then** Set aspect to `Stop` and `Exit` **Else** `Continue`.
    2. **If** Downstream Mast’s Track Circuit indicates `Stop`, **Then** Set aspect to `Approach` and `Continue` **Else** Set aspect to `Clear`and `Continue`.

- **Logic Processing** determines what happens after the a logic statement is processed, `Exit` to stop processing the logic statements in the group, or `Continue` to continue with the next logic statement (e.g. additional conditions need to be evaluated and aspects set).  Note that processing the last logic statement in the group will automatically exit the group upon completion.

- **Track Circuit**:  Track Circuits report the downstream track speed as shown by a mast linked to the track, simplifying the number of conditions that need checking and are particularly useful when dealing with downstream masts.  During configuration, a track circuit is used as a variable in the conditions.  For example, when the downstream signal aspect is reporting a stop speed, the current mast typically would show an approach speed.

  - Planning example: **If** Downstream Mast’s Track Circuit indicates `Stop`, **Then** Set aspect to `Approach` and `Continue` **Else** Set aspect to `Clear`and `Continue`.

## Ordering Conditionals

When crafting a logic statement for a signal, it is standard practice to first assess conditions that necessitate the most restrictive track speed (e.g., Stop), followed by conditions for intermediate speeds (e.g., Approach), and lastly, conditions allowing the least restrictive speeds (e.g., Clear).

## Signal Aspect Configuration Summary

The following table is provided to assist in simplifying the configuration of signal aspects.  The configurations are listed based on the number of signal aspects to be set (heads and lamps) and what is influences the aspect downstream of the signal (blocks, turnouts, masts).

To futher simplify the planning:

1. only three aspects are define; `Stop`, `Approach`, and `Clear`.  
2. check for all conditions that set the aspect to `Stop`, followed by conditions for `Approach`, and finally `Clear`.
3. even thought configuring aspects requires configuring the indications, the setting of the lamps is not defined below since that varies by the aspect rules and signal head type.
4. utilize the minimum necessary number of logic statements. 
5. track circuits are used to check for downstream track speeds

Note that up to 4 actions can be executed for true and false conditions, allowing for a **tumble-down** to be configured for setting up to 4 aspects.  For example, when configuring the first signal located at the beginning of a set of blocks between sidings (headblock), configure multiple actions for this signal where each action sets the same aspect downstream signals, thus creating a tumple-down of the signals being set (all appear the same).   

The use of `Exit` and `Continue` within the logic statements' actions signals whether the logic processing for that group should cease ('Exit') or proceed to evaluate the next logic statement ('Continue'). Generally, once the appropriate aspect is displayed based on the evaluated conditions, the logic processing for that group concludes.  

| **Signal Mast Configuration**        | **Downstream Elements**                     | **Logic Group (one or more logic statements)**               | Visual                                                       |
| ------------------------------------ | ------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Single 2-Lamp Head**               | 1 Block, 1 Masts, 0 Turnouts                | 1. **If** Block is Occupied, **Then** Set aspect to `Stop` and `Continue` **Else** Set aspect to `Clear` and `Continue`. | <img src="/assets/images/Setup/Signal_Single_2-Lamp.png" style="zoom: 200%;" /> |
| **Single 3-Lamp Head**               | 1 Block, 2 Mast, 0 Turnouts                 | 1. **If** Block is Occupied, **Then** Set aspect to `Stop` and `Exit`**Else** `Continue`. <br>2. **If** Downstream Mast shows `Stop`, **Then** Set aspect to `Approach` and `Continue` **Else** Set aspect to `Clear`and `Continue`. | <img src="/assets/images/Setup/Signal_Single_3-Lamp.png" style="zoom: 200%;" /> |
| **3-Lamp Head over 2-Lamp Head**     | 3 Blocks, 3 Masts, 1 Turnout                | 1. **If** Turnout Block is Occupied, **Then** Set Upper Head aspect to `Stop`, Lower Head aspect to `Stop`, and `Exit` **Else** `Continue`.<br>2. **If** Turnout is `Thrown`, **Then** Set Upper Head to `Stop` and `Continue` **Else** `Continue`<br>3. **If** Downstream Mast shows NOT`Clear` **Then** Set Upper Head aspect to `Approach` and `Continue` **Else** Set Upper Head aspect to `Clear` and `Continue`.<br>4. **If** Turnout is `Closed` OR Divergent Mast shows NOT `Clear`, **Then** Set Lower Head aspect to `Stop` and `Continue` **Else** Set Lower Head aspect to `Clear` and `Continue` | <img src="/assets/images/Setup/Signal_Double_3-Lamp_2-Lamp.png" style="zoom:200%;" /> |
| **3-Lamp Head over 3-Lamp Head**     | 2 Blocks, 2 Masts, 1 Turnout                | 1. **If** Turnout is Diverging, **Then** Upper Head Red, Lower Head Green for Diverging Route;<br>2. **If** First Block is Occupied, **Then** Upper Head Red, Lower Head Yellow;<br>3. **Else** Upper Head Green, Lower Head Green; |                                                              |
| **2-Lamp Head over 2-Lamp Head**     | 1 Block, 1 Mast, 1 Turnout (Diverging)      | 1. **If** Turnout is Diverging, **Then** Upper Head Red, Lower Head Green;<br>2. **If** Block is Occupied, **Then** Both Heads Red;<br>3. **Else** Both Heads Green; |                                                              |
| **Twin 3-Lamp Heads (Side by Side)** | 2 Blocks, 2 Masts, 2 Turnouts               | 1. **If** Either Turnout is Diverging, **Then** Corresponding Head Shows Yellow;<br>2. **If** Either Block is Occupied, **Then** Corresponding Head Shows Red;<br>3. **Else** Both Heads Show Green; |                                                              |
| **2-Lamp Head over 3-Lamp Head**     | 1 Block, 2 Masts, 1 Turnout                 | 1. **If** Turnout is Diverging, **Then** Upper Head Green, Lower Head Yellow;<br>2. **If** Block is Occupied, **Then** Upper Head Red, Lower Head Red;<br>3. **Else** Upper Head Green, Lower Head Green; |                                                              |
| **Dwarf Signal, 3-Lamp**             | 1 Block, 0 Masts, 1 Turnout (Diverging)     | 1. **If** Turnout is Diverging **And** Block is Occupied, **Then** Display Red;<br>2. **If** Turnout is Diverging, **Then** Display Yellow;<br>3. **Else** Display Green; |                                                              |
| **Vertical Stack of 3-Lamp Heads**   | 3 Blocks, 3 Masts, Multiple Turnouts        | 1. **If** Any Turnout is Diverging, **Then** Corresponding Head Red;<br>2. **If** Any Block is Occupied, **Then** Corresponding Head Yellow;<br>3. **Else** All Heads Green; |                                                              |
| **4-Lamp Head (Single or Multiple)** | Specialty areas like speed-controlled zones | 1. **If** Speed Restriction in Place, **Then** Display Aspect According to Restriction;<br>2. **If** Block Ahead is Occupied, **Then** Display Yellow;<br>3. **Else** Display Green; |                                                              |

